"""Run one small lesson; no API requests unless --live is explicitly supplied."""

import argparse
import asyncio
import json
import os
import re
import sys

from pydantic import BaseModel

from lab.runtime import Runtime
from lessons import (
    basic,
    collaboration,
    context,
    safety,
    sessions,
    structured,
    tools,
    workflow,
)

LESSONS = {
    1: ("Agent 与 Runner", basic),
    2: ("Function Tool 与调用循环", tools),
    3: ("本地 Context 与模型上下文", context),
    4: ("结构化输出", structured),
    5: ("Handoff 对比 Agent-as-Tool", collaboration),
    6: ("Session 与跨轮历史", sessions),
    7: ("Guardrail 与 max_turns 失败实验", safety),
    8: ("完整学习助手：Streaming + Hooks", workflow),
}


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    selection = result.add_mutually_exclusive_group()
    selection.add_argument("--lesson", type=int, choices=LESSONS, default=1)
    selection.add_argument("--all", action="store_true", help="离线运行全部八课")
    result.add_argument(
        "--live", action="store_true", help="显式允许真实 OpenAI API 调用和计费"
    )
    result.add_argument("--session-id", help="可选：第 6/8 课保存本地 SQLite 历史")
    return result


def display(result):
    if isinstance(result, tuple):
        for part in result:
            display(part)
        return
    if isinstance(result, dict):
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    output = result.final_output
    print(output.model_dump_json(indent=2) if isinstance(output, BaseModel) else output)
    print("last_agent:", result.last_agent.name)
    print("items:", " -> ".join(item.type for item in result.new_items))
    usage = result.context_wrapper.usage
    print(
        f"usage: requests={usage.requests}, input_tokens={usage.input_tokens}, "
        f"output_tokens={usage.output_tokens}"
    )


async def execute(args):
    rt = Runtime(
        live=args.live,
        model_name=os.environ.get("OPENAI_MODEL", "").strip(),
        session_id=args.session_id,
        on_event=lambda event: print("event:", event),
    )
    try:
        for number in LESSONS if args.all else [args.lesson]:
            title, lesson = LESSONS[number]
            print(
                f"\n=== {number:02d} {title} [{'LIVE / 可能计费' if rt.live else 'OFFLINE / 模型脚本'}] ==="
            )
            # A wall-clock deadline is distinct from model turns and per-request timeout.
            result = await asyncio.wait_for(lesson.run(rt), timeout=90)
            display(result)
        rt.assert_complete()
        if not rt.live:
            calls = sum(len(model.calls) for model in rt.models)
            print(
                f"\n离线模型调用次数={calls}；token usage 为合成值，不代表费用或模型质量。"
            )
    finally:
        await rt.close()


def main(argv=None):
    argument_parser = parser()
    args = argument_parser.parse_args(argv)
    if args.live and (args.all or args.lesson == 7):
        argument_parser.error("真实模式只允许单课 1～6 或 8；第 7 课故意触发失败。")
    if args.session_id and not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", args.session_id):
        argument_parser.error("session-id 只允许 1～64 位字母、数字、下划线或短横线。")
    try:
        asyncio.run(execute(args))
    except ValueError:
        print(
            "配置或输入不合法：真实模式请设置 OPENAI_API_KEY 和 OPENAI_MODEL。",
            file=sys.stderr,
        )
        return 2
    except KeyboardInterrupt:
        print("已中断本地等待；远端请求不保证未计费。", file=sys.stderr)
        return 130
    except Exception as error:
        # Avoid dumping provider bodies/headers or credentials in beginner logs.
        print(
            f"运行未完成：{type(error).__name__}。请查看 README 的排错说明。",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
