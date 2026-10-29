# 官方 DataCite 原件：首批两身份

2026-10-25实际 GET 精确doi API。以下保留响应，不是另外要求的状态账本。

```json
[
  {
    "data": {
      "id": "10.48550/arxiv.2606.06147",
      "type": "dois",
      "attributes": {
        "doi": "10.48550/arxiv.2606.06147",
        "prefix": "10.48550",
        "suffix": "arxiv.2606.06147",
        "identifiers": [
          {
            "identifier": "2606.06147",
            "identifierType": "arXiv"
          }
        ],
        "alternateIdentifiers": [
          {
            "alternateIdentifierType": "arXiv",
            "alternateIdentifier": "2606.06147"
          }
        ],
        "creators": [
          {
            "name": "Zheng, Shengtao",
            "nameType": "Personal",
            "givenName": "Shengtao",
            "familyName": "Zheng",
            "affiliation": [],
            "nameIdentifiers": []
          },
          {
            "name": "Li, Kai",
            "nameType": "Personal",
            "givenName": "Kai",
            "familyName": "Li",
            "affiliation": [],
            "nameIdentifiers": []
          },
          {
            "name": "Zhang, Weichen",
            "nameType": "Personal",
            "givenName": "Weichen",
            "familyName": "Zhang",
            "affiliation": [],
            "nameIdentifiers": []
          },
          {
            "name": "Meng, Yu",
            "nameType": "Personal",
            "givenName": "Yu",
            "familyName": "Meng",
            "affiliation": [],
            "nameIdentifiers": []
          },
          {
            "name": "Gao, Chen",
            "nameType": "Personal",
            "givenName": "Chen",
            "familyName": "Gao",
            "affiliation": [],
            "nameIdentifiers": []
          },
          {
            "name": "Chen, Xinlei",
            "nameType": "Personal",
            "givenName": "Xinlei",
            "familyName": "Chen",
            "affiliation": [],
            "nameIdentifiers": []
          },
          {
            "name": "Li, Yong",
            "nameType": "Personal",
            "givenName": "Yong",
            "familyName": "Li",
            "affiliation": [],
            "nameIdentifiers": []
          },
          {
            "name": "Zhang, Xiao-Ping",
            "nameType": "Personal",
            "givenName": "Xiao-Ping",
            "familyName": "Zhang",
            "affiliation": [],
            "nameIdentifiers": []
          }
        ],
        "titles": [
          {
            "title": "WorldFly: A World-Model-Based Vision-Language-Action Model for UAV Navigation"
          }
        ],
        "publisher": "arXiv",
        "container": {},
        "publicationYear": 2026,
        "subjects": [
          {
            "lang": "en",
            "subject": "Artificial Intelligence (cs.AI)",
            "subjectScheme": "arXiv"
          },
          {
            "subject": "FOS: Computer and information sciences",
            "subjectScheme": "Fields of Science and Technology (FOS)"
          },
          {
            "subject": "FOS: Computer and information sciences",
            "schemeUri": "http://www.oecd.org/science/inno/38235147.pdf",
            "subjectScheme": "Fields of Science and Technology (FOS)"
          }
        ],
        "contributors": [],
        "dates": [
          {
            "date": "2026-06-04T13:23:05Z",
            "dateType": "Submitted",
            "dateInformation": "v1"
          },
          {
            "date": "2026-06-05T00:58:47Z",
            "dateType": "Updated",
            "dateInformation": "v1"
          },
          {
            "date": "2026-06",
            "dateType": "Available",
            "dateInformation": "v1"
          },
          {
            "date": "2026",
            "dateType": "Issued"
          }
        ],
        "language": null,
        "types": {
          "ris": "GEN",
          "bibtex": "misc",
          "citeproc": "article",
          "schemaOrg": "CreativeWork",
          "resourceType": "Article",
          "resourceTypeGeneral": "Preprint"
        },
        "relatedIdentifiers": [],
        "relatedItems": [],
        "sizes": [],
        "formats": [],
        "version": "1",
        "rightsList": [
          {
            "rights": "arXiv.org perpetual, non-exclusive license",
            "rightsUri": "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"
          }
        ],
        "descriptions": [
          {
            "description": "End-to-end Vision-Language-Action (VLA) models have shown promise in UAV navigation. However, existing approaches typically rely on historical observations to directly predict actions, often struggling in dense urban environments where severe occlusions and sharp turns result in drastic viewpoint transitions. We argue that the ability to \"imagine\" future states -- inherent in World Models -- is critical for robust decision-making under such partial observability. To address this, we construct a challenging Urban Canyon Traversal Benchmark, specifically designed to evaluate spatial understanding in scenarios characterized by severe occlusions and drastic viewpoint transitions. To this end, we propose WorldFly, a novel world-model-based VLA framework that employs a dual-branch coupled flow matching mechanism to jointly generate future video predictions and navigation actions, thereby explicitly guiding the agent's policy via spatial imagination. Extensive evaluations on our benchmark demonstrate that WorldFly outperforms other baselines, particularly in unseen environments, validating the effectiveness of integrating world models into embodied aerial agents.",
            "descriptionType": "Abstract"
          }
        ],
        "geoLocations": [],
        "fundingReferences": [],
        "xml": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHJlc291cmNlIHhtbG5zPSJodHRwOi8vZGF0YWNpdGUub3JnL3NjaGVtYS9rZXJuZWwtNCIgeG1sbnM6eHNpPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZSIgeHNpOnNjaGVtYUxvY2F0aW9uPSJodHRwOi8vZGF0YWNpdGUub3JnL3NjaGVtYS9rZXJuZWwtNCBodHRwOi8vc2NoZW1hLmRhdGFjaXRlLm9yZy9tZXRhL2tlcm5lbC00LjMvbWV0YWRhdGEueHNkIj4KICA8aWRlbnRpZmllciBpZGVudGlmaWVyVHlwZT0iRE9JIj4xMC40ODU1MC9BUlhJVi4yNjA2LjA2MTQ3PC9pZGVudGlmaWVyPgogIDxhbHRlcm5hdGVJZGVudGlmaWVycz4KICAgIDxhbHRlcm5hdGVJZGVudGlmaWVyIGFsdGVybmF0ZUlkZW50aWZpZXJUeXBlPSJhclhpdiI+MjYwNi4wNjE0NzwvYWx0ZXJuYXRlSWRlbnRpZmllcj4KICA8L2FsdGVybmF0ZUlkZW50aWZpZXJzPgogIDxjcmVhdG9ycz4KICAgIDxjcmVhdG9yPgogICAgICA8Y3JlYXRvck5hbWUgbmFtZVR5cGU9IlBlcnNvbmFsIj5aaGVuZywgU2hlbmd0YW88L2NyZWF0b3JOYW1lPgogICAgICA8Z2l2ZW5OYW1lPlNoZW5ndGFvPC9naXZlbk5hbWU+CiAgICAgIDxmYW1pbHlOYW1lPlpoZW5nPC9mYW1pbHlOYW1lPgogICAgPC9jcmVhdG9yPgogICAgPGNyZWF0b3I+CiAgICAgIDxjcmVhdG9yTmFtZSBuYW1lVHlwZT0iUGVyc29uYWwiPkxpLCBLYWk8L2NyZWF0b3JOYW1lPgogICAgICA8Z2l2ZW5OYW1lPkthaTwvZ2l2ZW5OYW1lPgogICAgICA8ZmFtaWx5TmFtZT5MaTwvZmFtaWx5TmFtZT4KICAgIDwvY3JlYXRvcj4KICAgIDxjcmVhdG9yPgogICAgICA8Y3JlYXRvck5hbWUgbmFtZVR5cGU9IlBlcnNvbmFsIj5aaGFuZywgV2VpY2hlbjwvY3JlYXRvck5hbWU+CiAgICAgIDxnaXZlbk5hbWU+V2VpY2hlbjwvZ2l2ZW5OYW1lPgogICAgICA8ZmFtaWx5TmFtZT5aaGFuZzwvZmFtaWx5TmFtZT4KICAgIDwvY3JlYXRvcj4KICAgIDxjcmVhdG9yPgogICAgICA8Y3JlYXRvck5hbWUgbmFtZVR5cGU9IlBlcnNvbmFsIj5NZW5nLCBZdTwvY3JlYXRvck5hbWU+CiAgICAgIDxnaXZlbk5hbWU+WXU8L2dpdmVuTmFtZT4KICAgICAgPGZhbWlseU5hbWU+TWVuZzwvZmFtaWx5TmFtZT4KICAgIDwvY3JlYXRvcj4KICAgIDxjcmVhdG9yPgogICAgICA8Y3JlYXRvck5hbWUgbmFtZVR5cGU9IlBlcnNvbmFsIj5HYW8sIENoZW48L2NyZWF0b3JOYW1lPgogICAgICA8Z2l2ZW5OYW1lPkNoZW48L2dpdmVuTmFtZT4KICAgICAgPGZhbWlseU5hbWU+R2FvPC9mYW1pbHlOYW1lPgogICAgPC9jcmVhdG9yPgogICAgPGNyZWF0b3I+CiAgICAgIDxjcmVhdG9yTmFtZSBuYW1lVHlwZT0iUGVyc29uYWwiPkNoZW4sIFhpbmxlaTwvY3JlYXRvck5hbWU+CiAgICAgIDxnaXZlbk5hbWU+WGlubGVpPC9naXZlbk5hbWU+CiAgICAgIDxmYW1pbHlOYW1lPkNoZW48L2ZhbWlseU5hbWU+CiAgICA8L2NyZWF0b3I+CiAgICA8Y3JlYXRvcj4KICAgICAgPGNyZWF0b3JOYW1lIG5hbWVUeXBlPSJQZXJzb25hbCI+TGksIFlvbmc8L2NyZWF0b3JOYW1lPgogICAgICA8Z2l2ZW5OYW1lPllvbmc8L2dpdmVuTmFtZT4KICAgICAgPGZhbWlseU5hbWU+TGk8L2ZhbWlseU5hbWU+CiAgICA8L2NyZWF0b3I+CiAgICA8Y3JlYXRvcj4KICAgICAgPGNyZWF0b3JOYW1lIG5hbWVUeXBlPSJQZXJzb25hbCI+WmhhbmcsIFhpYW8tUGluZzwvY3JlYXRvck5hbWU+CiAgICAgIDxnaXZlbk5hbWU+WGlhby1QaW5nPC9naXZlbk5hbWU+CiAgICAgIDxmYW1pbHlOYW1lPlpoYW5nPC9mYW1pbHlOYW1lPgogICAgPC9jcmVhdG9yPgogIDwvY3JlYXRvcnM+CiAgPHRpdGxlcz4KICAgIDx0aXRsZT5Xb3JsZEZseTogQSBXb3JsZC1Nb2RlbC1CYXNlZCBWaXNpb24tTGFuZ3VhZ2UtQWN0aW9uIE1vZGVsIGZvciBVQVYgTmF2aWdhdGlvbjwvdGl0bGU+CiAgPC90aXRsZXM+CiAgPHB1Ymxpc2hlcj5hclhpdjwvcHVibGlzaGVyPgogIDxwdWJsaWNhdGlvblllYXI+MjAyNjwvcHVibGljYXRpb25ZZWFyPgogIDxzdWJqZWN0cz4KICAgIDxzdWJqZWN0IHhtbDpsYW5nPSJlbiIgc3ViamVjdFNjaGVtZT0iYXJYaXYiPkFydGlmaWNpYWwgSW50ZWxsaWdlbmNlIChjcy5BSSk8L3N1YmplY3Q+CiAgICA8c3ViamVjdCBzdWJqZWN0U2NoZW1lPSJGaWVsZHMgb2YgU2NpZW5jZSBhbmQgVGVjaG5vbG9neSAoRk9TKSI+Rk9TOiBDb21wdXRlciBhbmQgaW5mb3JtYXRpb24gc2NpZW5jZXM8L3N1YmplY3Q+CiAgPC9zdWJqZWN0cz4KICA8ZGF0ZXM+CiAgICA8ZGF0ZSBkYXRlVHlwZT0iU3VibWl0dGVkIiBkYXRlSW5mb3JtYXRpb249InYxIj4yMDI2LTA2LTA0VDEzOjIzOjA1WjwvZGF0ZT4KICAgIDxkYXRlIGRhdGVUeXBlPSJVcGRhdGVkIiBkYXRlSW5mb3JtYXRpb249InYxIj4yMDI2LTA2LTA1VDAwOjU4OjQ3WjwvZGF0ZT4KICAgIDxkYXRlIGRhdGVUeXBlPSJBdmFpbGFibGUiIGRhdGVJbmZvcm1hdGlvbj0idjEiPjIwMjYtMDY8L2RhdGU+CiAgPC9kYXRlcz4KICA8cmVzb3VyY2VUeXBlIHJlc291cmNlVHlwZUdlbmVyYWw9IlByZXByaW50Ij5BcnRpY2xlPC9yZXNvdXJjZVR5cGU+CiAgPHZlcnNpb24+MTwvdmVyc2lvbj4KICA8cmlnaHRzTGlzdD4KICAgIDxyaWdodHMgcmlnaHRzVVJJPSJodHRwOi8vYXJ4aXYub3JnL2xpY2Vuc2VzL25vbmV4Y2x1c2l2ZS1kaXN0cmliLzEuMC8iPmFyWGl2Lm9yZyBwZXJwZXR1YWwsIG5vbi1leGNsdXNpdmUgbGljZW5zZTwvcmlnaHRzPgogIDwvcmlnaHRzTGlzdD4KICA8ZGVzY3JpcHRpb25zPgogICAgPGRlc2NyaXB0aW9uIGRlc2NyaXB0aW9uVHlwZT0iQWJzdHJhY3QiPkVuZC10by1lbmQgVmlzaW9uLUxhbmd1YWdlLUFjdGlvbiAoVkxBKSBtb2RlbHMgaGF2ZSBzaG93biBwcm9taXNlIGluIFVBViBuYXZpZ2F0aW9uLiBIb3dldmVyLCBleGlzdGluZyBhcHByb2FjaGVzIHR5cGljYWxseSByZWx5IG9uIGhpc3RvcmljYWwgb2JzZXJ2YXRpb25zIHRvIGRpcmVjdGx5IHByZWRpY3QgYWN0aW9ucywgb2Z0ZW4gc3RydWdnbGluZyBpbiBkZW5zZSB1cmJhbiBlbnZpcm9ubWVudHMgd2hlcmUgc2V2ZXJlIG9jY2x1c2lvbnMgYW5kIHNoYXJwIHR1cm5zIHJlc3VsdCBpbiBkcmFzdGljIHZpZXdwb2ludCB0cmFuc2l0aW9ucy4gV2UgYXJndWUgdGhhdCB0aGUgYWJpbGl0eSB0byAiaW1hZ2luZSIgZnV0dXJlIHN0YXRlcyAtLSBpbmhlcmVudCBpbiBXb3JsZCBNb2RlbHMgLS0gaXMgY3JpdGljYWwgZm9yIHJvYnVzdCBkZWNpc2lvbi1tYWtpbmcgdW5kZXIgc3VjaCBwYXJ0aWFsIG9ic2VydmFiaWxpdHkuIFRvIGFkZHJlc3MgdGhpcywgd2UgY29uc3RydWN0IGEgY2hhbGxlbmdpbmcgVXJiYW4gQ2FueW9uIFRyYXZlcnNhbCBCZW5jaG1hcmssIHNwZWNpZmljYWxseSBkZXNpZ25lZCB0byBldmFsdWF0ZSBzcGF0aWFsIHVuZGVyc3RhbmRpbmcgaW4gc2NlbmFyaW9zIGNoYXJhY3Rlcml6ZWQgYnkgc2V2ZXJlIG9jY2x1c2lvbnMgYW5kIGRyYXN0aWMgdmlld3BvaW50IHRyYW5zaXRpb25zLiBUbyB0aGlzIGVuZCwgd2UgcHJvcG9zZSBXb3JsZEZseSwgYSBub3ZlbCB3b3JsZC1tb2RlbC1iYXNlZCBWTEEgZnJhbWV3b3JrIHRoYXQgZW1wbG95cyBhIGR1YWwtYnJhbmNoIGNvdXBsZWQgZmxvdyBtYXRjaGluZyBtZWNoYW5pc20gdG8gam9pbnRseSBnZW5lcmF0ZSBmdXR1cmUgdmlkZW8gcHJlZGljdGlvbnMgYW5kIG5hdmlnYXRpb24gYWN0aW9ucywgdGhlcmVieSBleHBsaWNpdGx5IGd1aWRpbmcgdGhlIGFnZW50J3MgcG9saWN5IHZpYSBzcGF0aWFsIGltYWdpbmF0aW9uLiBFeHRlbnNpdmUgZXZhbHVhdGlvbnMgb24gb3VyIGJlbmNobWFyayBkZW1vbnN0cmF0ZSB0aGF0IFdvcmxkRmx5IG91dHBlcmZvcm1zIG90aGVyIGJhc2VsaW5lcywgcGFydGljdWxhcmx5IGluIHVuc2VlbiBlbnZpcm9ubWVudHMsIHZhbGlkYXRpbmcgdGhlIGVmZmVjdGl2ZW5lc3Mgb2YgaW50ZWdyYXRpbmcgd29ybGQgbW9kZWxzIGludG8gZW1ib2RpZWQgYWVyaWFsIGFnZW50cy48L2Rlc2NyaXB0aW9uPgogIDwvZGVzY3JpcHRpb25zPgo8L3Jlc291cmNlPg==",
        "url": "https://arxiv.org/abs/2606.06147",
        "contentUrl": null,
        "metadataVersion": 0,
        "schemaVersion": "http://datacite.org/schema/kernel-4",
        "source": "mds",
        "isActive": true,
        "state": "findable",
        "reason": null,
        "viewCount": 0,
        "viewsOverTime": [],
        "downloadCount": 0,
        "downloadsOverTime": [],
        "referenceCount": 0,
        "citationCount": 0,
        "citationsOverTime": [],
        "partCount": 0,
        "partOfCount": 0,
        "versionCount": 0,
        "versionOfCount": 0,
        "created": "2026-06-05T02:16:41.000Z",
        "registered": "2026-06-05T02:16:41.000Z",
        "published": "2026",
        "updated": "2026-06-05T02:16:41.000Z"
      },
      "relationships": {
        "client": {
          "data": {
            "id": "arxiv.content",
            "type": "clients"
          }
        },
        "provider": {
          "data": {
            "id": "arxiv",
            "type": "providers"
          }
        },
        "media": {
          "data": {
            "id": "10.48550/arxiv.2606.06147",
            "type": "media"
          }
        },
        "references": {
          "data": []
        },
        "citations": {
          "data": []
        },
        "parts": {
          "data": []
        },
        "partOf": {
          "data": []
        },
        "versions": {
          "data": []
        },
        "versionOf": {
          "data": []
        }
      }
    }
  },
  {
    "data": {
      "id": "10.48550/arxiv.2606.05564",
      "type": "dois",
      "attributes": {
        "doi": "10.48550/arxiv.2606.05564",
        "prefix": "10.48550",
        "suffix": "arxiv.2606.05564",
        "identifiers": [
          {
            "identifier": "2606.05564",
            "identifierType": "arXiv"
          }
        ],
        "alternateIdentifiers": [
          {
            "alternateIdentifierType": "arXiv",
            "alternateIdentifier": "2606.05564"
          }
        ],
        "creators": [
          {
            "name": "Aggarwal, Varun",
            "nameType": "Personal",
            "givenName": "Varun",
            "familyName": "Aggarwal",
            "affiliation": [],
            "nameIdentifiers": []
          },
          {
            "name": "Kobak, Kay",
            "nameType": "Personal",
            "givenName": "Kay",
            "familyName": "Kobak",
            "affiliation": [],
            "nameIdentifiers": []
          },
          {
            "name": "Howarter, John",
            "nameType": "Personal",
            "givenName": "John",
            "familyName": "Howarter",
            "affiliation": [],
            "nameIdentifiers": []
          }
        ],
        "titles": [
          {
            "title": "Using Large Language Models to Support High Volume Application Review for an Undergraduate Research Program"
          }
        ],
        "publisher": "arXiv",
        "container": {},
        "publicationYear": 2026,
        "subjects": [
          {
            "lang": "en",
            "subject": "Computation and Language (cs.CL)",
            "subjectScheme": "arXiv"
          },
          {
            "subject": "FOS: Computer and information sciences",
            "subjectScheme": "Fields of Science and Technology (FOS)"
          },
          {
            "subject": "FOS: Computer and information sciences",
            "schemeUri": "http://www.oecd.org/science/inno/38235147.pdf",
            "subjectScheme": "Fields of Science and Technology (FOS)"
          }
        ],
        "contributors": [],
        "dates": [
          {
            "date": "2026-06-04T01:20:39Z",
            "dateType": "Submitted",
            "dateInformation": "v1"
          },
          {
            "date": "2026-06-05T00:23:05Z",
            "dateType": "Updated",
            "dateInformation": "v1"
          },
          {
            "date": "2026-06",
            "dateType": "Available",
            "dateInformation": "v1"
          },
          {
            "date": "2026",
            "dateType": "Issued"
          }
        ],
        "language": null,
        "types": {
          "ris": "GEN",
          "bibtex": "misc",
          "citeproc": "article",
          "schemaOrg": "CreativeWork",
          "resourceType": "Article",
          "resourceTypeGeneral": "Preprint"
        },
        "relatedIdentifiers": [],
        "relatedItems": [],
        "sizes": [],
        "formats": [],
        "version": "1",
        "rightsList": [
          {
            "rights": "arXiv.org perpetual, non-exclusive license",
            "rightsUri": "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"
          }
        ],
        "descriptions": [
          {
            "description": "Undergraduate research programs such as the Summer Undergraduate Research Fellowship (SURF) at Purdue University receive thousands of applications every year, requiring significant time and effort for program staff to evaluate each submission consistently and within tight timelines. This work-in-progress paper describes the development and initial deployment of a large language model (LLM)-based tool to assist in the evaluation of approximately 1,200 student Statements of Purpose (SoPs) for the SURF 2026 cycle at Purdue University. The workflow utilizes OpenAI GPT models (GPT-4o, GPT-5-mini, and GPT-5.2) and uses a structured rubric across six subcategories, each scored on a 0-3 scale. A few SoPs, graded by program staff, were used to tune the model responses. The model prompt was designed to generate both numerical scores, rationales (including positive and negative aspects) and short excerpts from each submission. Using GPT-5.2, the full batch of 1,200 SoPs was processed in approximately 4.6 hours of compute time, averaging roughly 14 seconds per SoP (with per-SoP timing varying with SoP length, which ranged from 500 to 2,000 words). Notable differences in rubric adherence were observed across model versions, with GPT-5.2 adhering most closely. Disagreement in model scores was more pronounced for lower-scoring submissions. The LLM outputs replicated the role previously played by distributed human graders, providing the program coordinator with scored and rationale-annotated outputs for the entire applicant pool. The program coordinator then reviewed these outputs alongside each applicant's SoP, applying the same downstream office criteria used in prior SURF cycles, to produce a shortlist of strong candidates. This coordinator review was completed in approximately 4 hours, compared to the multi-week coordination effort required in prior program cycles.",
            "descriptionType": "Abstract"
          }
        ],
        "geoLocations": [],
        "fundingReferences": [],
        "xml": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHJlc291cmNlIHhtbG5zPSJodHRwOi8vZGF0YWNpdGUub3JnL3NjaGVtYS9rZXJuZWwtNCIgeG1sbnM6eHNpPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZSIgeHNpOnNjaGVtYUxvY2F0aW9uPSJodHRwOi8vZGF0YWNpdGUub3JnL3NjaGVtYS9rZXJuZWwtNCBodHRwOi8vc2NoZW1hLmRhdGFjaXRlLm9yZy9tZXRhL2tlcm5lbC00LjMvbWV0YWRhdGEueHNkIj4KICA8aWRlbnRpZmllciBpZGVudGlmaWVyVHlwZT0iRE9JIj4xMC40ODU1MC9BUlhJVi4yNjA2LjA1NTY0PC9pZGVudGlmaWVyPgogIDxhbHRlcm5hdGVJZGVudGlmaWVycz4KICAgIDxhbHRlcm5hdGVJZGVudGlmaWVyIGFsdGVybmF0ZUlkZW50aWZpZXJUeXBlPSJhclhpdiI+MjYwNi4wNTU2NDwvYWx0ZXJuYXRlSWRlbnRpZmllcj4KICA8L2FsdGVybmF0ZUlkZW50aWZpZXJzPgogIDxjcmVhdG9ycz4KICAgIDxjcmVhdG9yPgogICAgICA8Y3JlYXRvck5hbWUgbmFtZVR5cGU9IlBlcnNvbmFsIj5BZ2dhcndhbCwgVmFydW48L2NyZWF0b3JOYW1lPgogICAgICA8Z2l2ZW5OYW1lPlZhcnVuPC9naXZlbk5hbWU+CiAgICAgIDxmYW1pbHlOYW1lPkFnZ2Fyd2FsPC9mYW1pbHlOYW1lPgogICAgPC9jcmVhdG9yPgogICAgPGNyZWF0b3I+CiAgICAgIDxjcmVhdG9yTmFtZSBuYW1lVHlwZT0iUGVyc29uYWwiPktvYmFrLCBLYXk8L2NyZWF0b3JOYW1lPgogICAgICA8Z2l2ZW5OYW1lPktheTwvZ2l2ZW5OYW1lPgogICAgICA8ZmFtaWx5TmFtZT5Lb2JhazwvZmFtaWx5TmFtZT4KICAgIDwvY3JlYXRvcj4KICAgIDxjcmVhdG9yPgogICAgICA8Y3JlYXRvck5hbWUgbmFtZVR5cGU9IlBlcnNvbmFsIj5Ib3dhcnRlciwgSm9objwvY3JlYXRvck5hbWU+CiAgICAgIDxnaXZlbk5hbWU+Sm9objwvZ2l2ZW5OYW1lPgogICAgICA8ZmFtaWx5TmFtZT5Ib3dhcnRlcjwvZmFtaWx5TmFtZT4KICAgIDwvY3JlYXRvcj4KICA8L2NyZWF0b3JzPgogIDx0aXRsZXM+CiAgICA8dGl0bGU+VXNpbmcgTGFyZ2UgTGFuZ3VhZ2UgTW9kZWxzIHRvIFN1cHBvcnQgSGlnaCBWb2x1bWUgQXBwbGljYXRpb24gUmV2aWV3IGZvciBhbiBVbmRlcmdyYWR1YXRlIFJlc2VhcmNoIFByb2dyYW08L3RpdGxlPgogIDwvdGl0bGVzPgogIDxwdWJsaXNoZXI+YXJYaXY8L3B1Ymxpc2hlcj4KICA8cHVibGljYXRpb25ZZWFyPjIwMjY8L3B1YmxpY2F0aW9uWWVhcj4KICA8c3ViamVjdHM+CiAgICA8c3ViamVjdCB4bWw6bGFuZz0iZW4iIHN1YmplY3RTY2hlbWU9ImFyWGl2Ij5Db21wdXRhdGlvbiBhbmQgTGFuZ3VhZ2UgKGNzLkNMKTwvc3ViamVjdD4KICAgIDxzdWJqZWN0IHN1YmplY3RTY2hlbWU9IkZpZWxkcyBvZiBTY2llbmNlIGFuZCBUZWNobm9sb2d5IChGT1MpIj5GT1M6IENvbXB1dGVyIGFuZCBpbmZvcm1hdGlvbiBzY2llbmNlczwvc3ViamVjdD4KICA8L3N1YmplY3RzPgogIDxkYXRlcz4KICAgIDxkYXRlIGRhdGVUeXBlPSJTdWJtaXR0ZWQiIGRhdGVJbmZvcm1hdGlvbj0idjEiPjIwMjYtMDYtMDRUMDE6MjA6MzlaPC9kYXRlPgogICAgPGRhdGUgZGF0ZVR5cGU9IlVwZGF0ZWQiIGRhdGVJbmZvcm1hdGlvbj0idjEiPjIwMjYtMDYtMDVUMDA6MjM6MDVaPC9kYXRlPgogICAgPGRhdGUgZGF0ZVR5cGU9IkF2YWlsYWJsZSIgZGF0ZUluZm9ybWF0aW9uPSJ2MSI+MjAyNi0wNjwvZGF0ZT4KICA8L2RhdGVzPgogIDxyZXNvdXJjZVR5cGUgcmVzb3VyY2VUeXBlR2VuZXJhbD0iUHJlcHJpbnQiPkFydGljbGU8L3Jlc291cmNlVHlwZT4KICA8dmVyc2lvbj4xPC92ZXJzaW9uPgogIDxyaWdodHNMaXN0PgogICAgPHJpZ2h0cyByaWdodHNVUkk9Imh0dHA6Ly9hcnhpdi5vcmcvbGljZW5zZXMvbm9uZXhjbHVzaXZlLWRpc3RyaWIvMS4wLyI+YXJYaXYub3JnIHBlcnBldHVhbCwgbm9uLWV4Y2x1c2l2ZSBsaWNlbnNlPC9yaWdodHM+CiAgPC9yaWdodHNMaXN0PgogIDxkZXNjcmlwdGlvbnM+CiAgICA8ZGVzY3JpcHRpb24gZGVzY3JpcHRpb25UeXBlPSJBYnN0cmFjdCI+VW5kZXJncmFkdWF0ZSByZXNlYXJjaCBwcm9ncmFtcyBzdWNoIGFzIHRoZSBTdW1tZXIgVW5kZXJncmFkdWF0ZSBSZXNlYXJjaCBGZWxsb3dzaGlwIChTVVJGKSBhdCBQdXJkdWUgVW5pdmVyc2l0eSByZWNlaXZlIHRob3VzYW5kcyBvZiBhcHBsaWNhdGlvbnMgZXZlcnkgeWVhciwgcmVxdWlyaW5nIHNpZ25pZmljYW50IHRpbWUgYW5kIGVmZm9ydCBmb3IgcHJvZ3JhbSBzdGFmZiB0byBldmFsdWF0ZSBlYWNoIHN1Ym1pc3Npb24gY29uc2lzdGVudGx5IGFuZCB3aXRoaW4gdGlnaHQgdGltZWxpbmVzLiBUaGlzIHdvcmstaW4tcHJvZ3Jlc3MgcGFwZXIgZGVzY3JpYmVzIHRoZSBkZXZlbG9wbWVudCBhbmQgaW5pdGlhbCBkZXBsb3ltZW50IG9mIGEgbGFyZ2UgbGFuZ3VhZ2UgbW9kZWwgKExMTSktYmFzZWQgdG9vbCB0byBhc3Npc3QgaW4gdGhlIGV2YWx1YXRpb24gb2YgYXBwcm94aW1hdGVseSAxLDIwMCBzdHVkZW50IFN0YXRlbWVudHMgb2YgUHVycG9zZSAoU29QcykgZm9yIHRoZSBTVVJGIDIwMjYgY3ljbGUgYXQgUHVyZHVlIFVuaXZlcnNpdHkuIFRoZSB3b3JrZmxvdyB1dGlsaXplcyBPcGVuQUkgR1BUIG1vZGVscyAoR1BULTRvLCBHUFQtNS1taW5pLCBhbmQgR1BULTUuMikgYW5kIHVzZXMgYSBzdHJ1Y3R1cmVkIHJ1YnJpYyBhY3Jvc3Mgc2l4IHN1YmNhdGVnb3JpZXMsIGVhY2ggc2NvcmVkIG9uIGEgMC0zIHNjYWxlLiBBIGZldyBTb1BzLCBncmFkZWQgYnkgcHJvZ3JhbSBzdGFmZiwgd2VyZSB1c2VkIHRvIHR1bmUgdGhlIG1vZGVsIHJlc3BvbnNlcy4gVGhlIG1vZGVsIHByb21wdCB3YXMgZGVzaWduZWQgdG8gZ2VuZXJhdGUgYm90aCBudW1lcmljYWwgc2NvcmVzLCByYXRpb25hbGVzIChpbmNsdWRpbmcgcG9zaXRpdmUgYW5kIG5lZ2F0aXZlIGFzcGVjdHMpIGFuZCBzaG9ydCBleGNlcnB0cyBmcm9tIGVhY2ggc3VibWlzc2lvbi4gVXNpbmcgR1BULTUuMiwgdGhlIGZ1bGwgYmF0Y2ggb2YgMSwyMDAgU29QcyB3YXMgcHJvY2Vzc2VkIGluIGFwcHJveGltYXRlbHkgNC42IGhvdXJzIG9mIGNvbXB1dGUgdGltZSwgYXZlcmFnaW5nIHJvdWdobHkgMTQgc2Vjb25kcyBwZXIgU29QICh3aXRoIHBlci1Tb1AgdGltaW5nIHZhcnlpbmcgd2l0aCBTb1AgbGVuZ3RoLCB3aGljaCByYW5nZWQgZnJvbSA1MDAgdG8gMiwwMDAgd29yZHMpLiBOb3RhYmxlIGRpZmZlcmVuY2VzIGluIHJ1YnJpYyBhZGhlcmVuY2Ugd2VyZSBvYnNlcnZlZCBhY3Jvc3MgbW9kZWwgdmVyc2lvbnMsIHdpdGggR1BULTUuMiBhZGhlcmluZyBtb3N0IGNsb3NlbHkuIERpc2FncmVlbWVudCBpbiBtb2RlbCBzY29yZXMgd2FzIG1vcmUgcHJvbm91bmNlZCBmb3IgbG93ZXItc2NvcmluZyBzdWJtaXNzaW9ucy4gVGhlIExMTSBvdXRwdXRzIHJlcGxpY2F0ZWQgdGhlIHJvbGUgcHJldmlvdXNseSBwbGF5ZWQgYnkgZGlzdHJpYnV0ZWQgaHVtYW4gZ3JhZGVycywgcHJvdmlkaW5nIHRoZSBwcm9ncmFtIGNvb3JkaW5hdG9yIHdpdGggc2NvcmVkIGFuZCByYXRpb25hbGUtYW5ub3RhdGVkIG91dHB1dHMgZm9yIHRoZSBlbnRpcmUgYXBwbGljYW50IHBvb2wuIFRoZSBwcm9ncmFtIGNvb3JkaW5hdG9yIHRoZW4gcmV2aWV3ZWQgdGhlc2Ugb3V0cHV0cyBhbG9uZ3NpZGUgZWFjaCBhcHBsaWNhbnQncyBTb1AsIGFwcGx5aW5nIHRoZSBzYW1lIGRvd25zdHJlYW0gb2ZmaWNlIGNyaXRlcmlhIHVzZWQgaW4gcHJpb3IgU1VSRiBjeWNsZXMsIHRvIHByb2R1Y2UgYSBzaG9ydGxpc3Qgb2Ygc3Ryb25nIGNhbmRpZGF0ZXMuIFRoaXMgY29vcmRpbmF0b3IgcmV2aWV3IHdhcyBjb21wbGV0ZWQgaW4gYXBwcm94aW1hdGVseSA0IGhvdXJzLCBjb21wYXJlZCB0byB0aGUgbXVsdGktd2VlayBjb29yZGluYXRpb24gZWZmb3J0IHJlcXVpcmVkIGluIHByaW9yIHByb2dyYW0gY3ljbGVzLjwvZGVzY3JpcHRpb24+CiAgPC9kZXNjcmlwdGlvbnM+CjwvcmVzb3VyY2U+",
        "url": "https://arxiv.org/abs/2606.05564",
        "contentUrl": null,
        "metadataVersion": 0,
        "schemaVersion": "http://datacite.org/schema/kernel-4",
        "source": "mds",
        "isActive": true,
        "state": "findable",
        "reason": null,
        "viewCount": 0,
        "viewsOverTime": [],
        "downloadCount": 0,
        "downloadsOverTime": [],
        "referenceCount": 0,
        "citationCount": 0,
        "citationsOverTime": [],
        "partCount": 0,
        "partOfCount": 0,
        "versionCount": 0,
        "versionOfCount": 0,
        "created": "2026-06-05T02:03:31.000Z",
        "registered": "2026-06-05T02:03:31.000Z",
        "published": "2026",
        "updated": "2026-06-05T02:03:31.000Z"
      },
      "relationships": {
        "client": {
          "data": {
            "id": "arxiv.content",
            "type": "clients"
          }
        },
        "provider": {
          "data": {
            "id": "arxiv",
            "type": "providers"
          }
        },
        "media": {
          "data": {
            "id": "10.48550/arxiv.2606.05564",
            "type": "media"
          }
        },
        "references": {
          "data": []
        },
        "citations": {
          "data": []
        },
        "parts": {
          "data": []
        },
        "partOf": {
          "data": []
        },
        "versions": {
          "data": []
        },
        "versionOf": {
          "data": []
        }
      }
    }
  }
]

```

