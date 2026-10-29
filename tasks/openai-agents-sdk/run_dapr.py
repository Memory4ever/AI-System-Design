"""Dapr 选修课入口：默认假状态库 + 真 SDK + 模型脚本，不接受 --live。"""

import argparse
import asyncio
import json
import os
import re
import sys

from lab.runtime import Runtime


async def execute(args):
    if args.sidecar:
        # 必须早于 Dapr 首次 import：其 settings 在导入时读取环境。
        # 同步构造器也会做 HTTP health check，不能只靠 asyncio.wait_for 限时。
        os.environ["DAPR_HTTP_ENDPOINT"] = "http://127.0.0.1:3500"
        os.environ["DAPR_HEALTH_TIMEOUT"] = "5"
        os.environ["DAPR_API_TIMEOUT_SECONDS"] = "5"
    # 延迟加载 optional extra，使 --help / 参数错误不依赖 Dapr 包。
    from agents.extensions.memory import DaprSession
    from lessons import dapr as lessons

    rt = Runtime()
    try:
        for number in [9, 10, 11] if args.all else [args.lesson]:
            mode = "LOCAL SIDECAR" if args.sidecar else "FAKE STATE"
            print(f"\n=== {number:02d} Dapr [{mode} / SCRIPTED MODEL] ===")
            if number == 9:
                lesson = lessons.state_basics()
            elif number == 11:
                lesson = lessons.conflict_boundary()
            else:
                factory = None
                if args.sidecar:
                    # 固定本机与教学 component；不接受任意远端 URL/业务 store。
                    # from_address 创建并拥有 client，async with 退出时负责关闭。
                    def factory():
                        return DaprSession.from_address(
                            f"agents-lab-dapr:{args.session_id}",
                            state_store_name=lessons.STORE,
                            dapr_address="127.0.0.1:50001",
                            ttl=3600,
                        )

                lesson = lessons.runner_history(rt, session_factory=factory)
            report = await asyncio.wait_for(lesson, timeout=30)
            print(json.dumps(report, ensure_ascii=False, indent=2))
        rt.assert_complete()
    finally:
        await rt.close()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--lesson", type=int, choices=[9, 10, 11], default=9)
    selection.add_argument("--all", action="store_true")
    parser.add_argument(
        "--sidecar", action="store_true", help="仅第 10 课，显式访问本机 Dapr"
    )
    parser.add_argument("--session-id", help="仅 sidecar 模式；1～32 位字母/数字/_/-")
    args = parser.parse_args(argv)
    if args.sidecar and (args.all or args.lesson != 10 or not args.session_id):
        parser.error(
            "sidecar 模式需要 --lesson 10 和显式 --session-id，不能与 --all 同用。"
        )
    if args.session_id and (
        not args.sidecar or not re.fullmatch(r"[A-Za-z0-9_-]{1,32}", args.session_id)
    ):
        parser.error(
            "session-id 只用于 sidecar；允许 1～32 位字母、数字、下划线、短横线。"
        )
    try:
        asyncio.run(execute(args))
    except ImportError:
        print("请先运行 uv sync --locked --extra dapr。", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        return 130
    except Exception as error:
        # 不把真实后端的地址、凭据、状态内容或异常响应体输出到教学日志。
        print(
            f"未完成：{type(error).__name__}；请看 DAPR.md 的排错与验证边界。",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
