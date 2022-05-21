#!/usr/bin/env python3
import requests
import json
import codecs

dict = {
  "kind": "youtube#searchListResponse",
  "etag": "DXQHflIjColj4x4AYJNMfr1Dm_w",
  "nextPageToken": "CAUQAA",
  "regionCode": "CZ",
  "pageInfo": {
    "totalResults": 1000000,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#searchResult",
      "etag": "bfuAsjPGSh-uLAgdfd-ak6V3o8A",
      "id": {
        "kind": "youtube#video",
        "videoId": "rfscVS0vtbw"
      },
      "snippet": {
        "publishedAt": "2018-07-11T18:00:42Z",
        "channelId": "UC8butISFwT-Wl7EV0hUK0BQ",
        "title": "Learn Python - Full Course for Beginners [Tutorial]",
        "description": "This course will give you a full introduction into all of the core concepts in python. Follow along with the videos and you'll be a ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/rfscVS0vtbw/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/rfscVS0vtbw/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/rfscVS0vtbw/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "freeCodeCamp.org",
        "liveBroadcastContent": "none",
        "publishTime": "2018-07-11T18:00:42Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "kSWECVuytUMH0reMhkfWZfhpMXs",
      "id": {
        "kind": "youtube#video",
        "videoId": "_uQrJ0TkZlc"
      },
      "snippet": {
        "publishedAt": "2019-02-18T15:00:08Z",
        "channelId": "UCWv7vMbMWH4-V0ZXdmDpPBA",
        "title": "Python Tutorial - Python Full Course for Beginners",
        "description": "Python tutorial - Python full course for beginners - Go from Zero to Hero with Python (includes machine learning & web ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/_uQrJ0TkZlc/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/_uQrJ0TkZlc/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/_uQrJ0TkZlc/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Programming with Mosh",
        "liveBroadcastContent": "none",
        "publishTime": "2019-02-18T15:00:08Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "a_jMWv3WbJengmqRHVFax3IsyFw",
      "id": {
        "kind": "youtube#video",
        "videoId": "qUG1olBSYk8"
      },
      "snippet": {
        "publishedAt": "2020-05-28T12:47:11Z",
        "channelId": "UCy2CD8IjM9-vOSTe9_VofOw",
        "title": "Python pro Začátečníky | #01 | Instalace",
        "description": "V prvním díle tutoriálu Python pro Začátečníky si ukážeme, jak nainstalovat Python Interpreter a Visual Studio Code. Python: ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/qUG1olBSYk8/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/qUG1olBSYk8/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/qUG1olBSYk8/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Conax",
        "liveBroadcastContent": "none",
        "publishTime": "2020-05-28T12:47:11Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "hoZiNvgBupiGUngdfDXrKtySxxE",
      "id": {
        "kind": "youtube#video",
        "videoId": "doZSkdlqsVY"
      },
      "snippet": {
        "publishedAt": "2019-11-21T11:06:25Z",
        "channelId": "UCqLHX-tRwt8dSgNgVSbyxLw",
        "title": "Programovanie (1) - prvá prednáška | úvod programovací jazyk Python",
        "description": "Programovanie (1) - prvá prednáška | úvod programovací jazyk Python 1-AIN-130/16 RNDr. Andrej Blaho, PhD.",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/doZSkdlqsVY/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/doZSkdlqsVY/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/doZSkdlqsVY/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "FMFI UK",
        "liveBroadcastContent": "none",
        "publishTime": "2019-11-21T11:06:25Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "uSlUNmuB3_5-yYTxDakdLAX_j7s",
      "id": {
        "kind": "youtube#video",
        "videoId": "kqtD5dpn9C8"
      },
      "snippet": {
        "publishedAt": "2020-09-16T13:00:20Z",
        "channelId": "UCWv7vMbMWH4-V0ZXdmDpPBA",
        "title": "Python for Beginners - Learn Python in 1 Hour",
        "description": "This Python tutorial for beginners show how to get started with Python quickly. Learn to code in 1 hour! Watch this tutorial get ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/kqtD5dpn9C8/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/kqtD5dpn9C8/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/kqtD5dpn9C8/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Programming with Mosh",
        "liveBroadcastContent": "none",
        "publishTime": "2020-09-16T13:00:20Z"
      }
    }
  ]
}

# print(dict)

for x in dict["items"]:
  print(x["id"]["videoId"])
foo = None