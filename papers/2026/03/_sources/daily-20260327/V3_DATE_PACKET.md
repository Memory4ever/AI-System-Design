# 03/27 有界公开时间恢复

实际官方availability170–186：ID/DOI不能预分配，Sun–Thu20Eastern公告且Submitted不是public；moderation1–4days可能延迟。ZoneInfoAmerica/New_York本轮Mar26T20=-04:00，即Mar27BJT08，Submitted全部晚Wed14EDT且早Thu14EDT，因此最早常规公开下界Mar27T08BJT。不宣称所有如期发布。

arxiv-ownedDOI findable注册可给保守upper，但本批registered全晚右端01Z，因此复合区间从Mar27BJT08到09:51..10:16跨日右端；不是已知窗外，更不是确定本窗。Updated v1未核到公开语义，不当upper（例如24755UpdatedMar30、25120May20、25378June10，普通metadata更新时间不是首公开证）。Available=March月精度。合法cs.DC2026-03show250实际412295B，仅monthheader，无分日公告；没有非法参数故障。一个官方OAI原请求 `https://export.arxiv.org/oai2?verb=GetRecord&metadataPrefix=arXivRaw&identifier=oai:arXiv.org:2603.24676` 实际3427B：datestamp=2026-03-27、versionv1/date=Wed,25Mar2026 18:00:29GMT，responseDate=2026-10-01T20:40:44Z；metadata日期/Submitted不证明公开时刻，因此有限停止，不扩arxiv实现/代码或全月分类重建。

## 首7原返回

```json
[
  {
    "id": "24676",
    "url": "https://api.datacite.org/dois/10.48550/arXiv.2603.24676",
    "state": "findable",
    "created": "2026-03-27T01:51:08.000Z",
    "registered": "2026-03-27T01:51:09.000Z",
    "client": {
      "data": {
        "id": "arxiv.content",
        "type": "clients"
      }
    },
    "dates": [
      {
        "date": "2026-03-25T18:00:29Z",
        "dateType": "Submitted",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03-27T00:02:07Z",
        "dateType": "Updated",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03",
        "dateType": "Available",
        "dateInformation": "v1"
      },
      {
        "date": "2026",
        "dateType": "Issued"
      }
    ]
  },
  {
    "id": "24755",
    "url": "https://api.datacite.org/dois/10.48550/arXiv.2603.24755",
    "state": "findable",
    "created": "2026-03-27T01:52:58.000Z",
    "registered": "2026-03-27T01:52:58.000Z",
    "client": {
      "data": {
        "id": "arxiv.content",
        "type": "clients"
      }
    },
    "dates": [
      {
        "date": "2026-03-25T19:26:44Z",
        "dateType": "Submitted",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03-30T00:55:44Z",
        "dateType": "Updated",
        "dateInformation": "v1"
      },
      {
        "date": "2026-05-07T20:39:58Z",
        "dateType": "Submitted",
        "dateInformation": "v2"
      },
      {
        "date": "2026-05-11T00:13:10Z",
        "dateType": "Updated",
        "dateInformation": "v2"
      },
      {
        "date": "2026-03",
        "dateType": "Available",
        "dateInformation": "v1"
      },
      {
        "date": "2026",
        "dateType": "Issued"
      }
    ]
  },
  {
    "id": "24775",
    "url": "https://api.datacite.org/dois/10.48550/arXiv.2603.24775",
    "state": "findable",
    "created": "2026-03-27T01:53:26.000Z",
    "registered": "2026-03-27T01:53:27.000Z",
    "client": {
      "data": {
        "id": "arxiv.content",
        "type": "clients"
      }
    },
    "dates": [
      {
        "date": "2026-03-25T19:45:37Z",
        "dateType": "Submitted",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03-27T00:07:54Z",
        "dateType": "Updated",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03",
        "dateType": "Available",
        "dateInformation": "v1"
      },
      {
        "date": "2026",
        "dateType": "Issued"
      }
    ]
  },
  {
    "id": "25056",
    "url": "https://api.datacite.org/dois/10.48550/arXiv.2603.25056",
    "state": "findable",
    "created": "2026-03-27T02:00:03.000Z",
    "registered": "2026-03-27T02:00:04.000Z",
    "client": {
      "data": {
        "id": "arxiv.content",
        "type": "clients"
      }
    },
    "dates": [
      {
        "date": "2026-03-26T05:48:37Z",
        "dateType": "Submitted",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03-27T00:30:05Z",
        "dateType": "Updated",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03",
        "dateType": "Available",
        "dateInformation": "v1"
      },
      {
        "date": "2026",
        "dateType": "Issued"
      }
    ]
  },
  {
    "id": "25284",
    "url": "https://api.datacite.org/dois/10.48550/arXiv.2603.25284",
    "state": "findable",
    "created": "2026-03-27T02:05:31.000Z",
    "registered": "2026-03-27T02:05:31.000Z",
    "client": {
      "data": {
        "id": "arxiv.content",
        "type": "clients"
      }
    },
    "dates": [
      {
        "date": "2026-03-26T10:21:38Z",
        "dateType": "Submitted",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03-27T00:44:21Z",
        "dateType": "Updated",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03",
        "dateType": "Available",
        "dateInformation": "v1"
      },
      {
        "date": "2026",
        "dateType": "Issued"
      }
    ]
  },
  {
    "id": "25716",
    "url": "https://api.datacite.org/dois/10.48550/arXiv.2603.25716",
    "state": "findable",
    "created": "2026-03-27T02:15:45.000Z",
    "registered": "2026-03-27T02:15:48.000Z",
    "client": {
      "data": {
        "id": "arxiv.content",
        "type": "clients"
      }
    },
    "dates": [
      {
        "date": "2026-03-26T17:56:01Z",
        "dateType": "Submitted",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03-27T01:11:42Z",
        "dateType": "Updated",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03-28T08:29:52Z",
        "dateType": "Submitted",
        "dateInformation": "v2"
      },
      {
        "date": "2026-03-31T00:28:11Z",
        "dateType": "Updated",
        "dateInformation": "v2"
      },
      {
        "date": "2026-03",
        "dateType": "Available",
        "dateInformation": "v1"
      },
      {
        "date": "2026",
        "dateType": "Issued"
      }
    ]
  },
  {
    "id": "24768",
    "url": "https://api.datacite.org/dois/10.48550/arXiv.2603.24768",
    "state": "findable",
    "created": "2026-03-27T01:53:16.000Z",
    "registered": "2026-03-27T01:53:17.000Z",
    "client": {
      "data": {
        "id": "arxiv.content",
        "type": "clients"
      }
    },
    "dates": [
      {
        "date": "2026-03-25T19:39:42Z",
        "dateType": "Submitted",
        "dateInformation": "v1"
      },
      {
        "date": "2026-03-27T00:07:41Z",
        "dateType": "Updated",
        "dateInformation": "v1"
      },
      {
        "date": "2026-05-07T16:27:28Z",
        "dateType": "Submitted",
        "dateInformation": "v2"
      },
      {
        "date": "2026-05-08T01:14:17Z",
        "dateType": "Updated",
        "dateInformation": "v2"
      },
      {
        "date": "2026-03",
        "dateType": "Available",
        "dateInformation": "v1"
      },
      {
        "date": "2026",
        "dateType": "Issued"
      }
    ]
  }
]
```

## 后23实际必要字段

公共接口 https://api.datacite.org/dois/10.48550/arXiv.2603.<ID> ，本轮实际响应字段抽取，仅保留已用下上界身份，不以版本Updated授权。24812最终范围关闭不请求日期。

```json
[
  {
    "id": "2603.24709v1",
    "Submitted": "2026-03-25T18:31:39Z",
    "registered": "2026-03-27T01:51:55.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.24917v1",
    "Submitted": "2026-03-26T01:15:16Z",
    "registered": "2026-03-27T01:56:49.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25001v1",
    "Submitted": "2026-03-26T04:02:23Z",
    "registered": "2026-03-27T01:58:45.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25011v1",
    "Submitted": "2026-03-26T04:20:24Z",
    "registered": "2026-03-27T01:58:59.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25120v1",
    "Submitted": "2026-03-26T07:45:29Z",
    "registered": "2026-03-27T02:01:37.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25158v1",
    "Submitted": "2026-03-26T08:26:38Z",
    "registered": "2026-03-27T02:02:33.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25164v1",
    "Submitted": "2026-03-26T08:30:18Z",
    "registered": "2026-03-27T02:02:42.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25412v1",
    "Submitted": "2026-03-26T13:08:56Z",
    "registered": "2026-03-27T02:08:34.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25674v1",
    "Submitted": "2026-03-26T17:29:20Z",
    "registered": "2026-03-27T02:14:47.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25702v1",
    "Submitted": "2026-03-26T17:48:50Z",
    "registered": "2026-03-27T02:15:26.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25723v1",
    "Submitted": "2026-03-26T17:58:15Z",
    "registered": "2026-03-27T02:15:57.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25727v1",
    "Submitted": "2026-03-26T17:59:03Z",
    "registered": "2026-03-27T02:16:03.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25378v1",
    "Submitted": "2026-03-26T12:28:54Z",
    "registered": "2026-03-27T02:07:45.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.24812v1",
    "Submitted": "2026-03-25T20:47:15Z",
    "registered": "2026-03-27T01:54:21.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.24680v1",
    "Submitted": "2026-03-25T18:01:19Z",
    "registered": "2026-03-27T01:51:14.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.24935v1",
    "Submitted": "2026-03-26T01:56:01Z",
    "registered": "2026-03-27T01:57:14.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.24984v1",
    "Submitted": "2026-03-26T03:23:45Z",
    "registered": "2026-03-27T01:58:22.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25077v1",
    "Submitted": "2026-03-26T06:25:27Z",
    "registered": "2026-03-27T02:00:35.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25661v1",
    "Submitted": "2026-03-26T17:14:57Z",
    "registered": "2026-03-27T02:14:29.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25583v1",
    "Submitted": "2026-03-26T16:00:39Z",
    "registered": "2026-03-27T02:12:38.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25403v1",
    "Submitted": "2026-03-26T12:53:49Z",
    "registered": "2026-03-27T02:08:21.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25685v1",
    "Submitted": "2026-03-26T17:36:08Z",
    "registered": "2026-03-27T02:15:03.000Z",
    "state": "findable",
    "client": "arxiv.content"
  },
  {
    "id": "2603.25074v1",
    "Submitted": "2026-03-26T06:24:28Z",
    "registered": "2026-03-27T02:00:31.000Z",
    "state": "findable",
    "client": "arxiv.content"
  }
]
```
