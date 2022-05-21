import requests
import codecs
import json
import os

googleapi = "https://www.googleapis.com/youtube/v3"
jsonpath = os.path.join(os.path.expanduser("~"), ".local", "share", "ytcli", "apikey.json")

def readKey():
    with open(jsonpath) as keyjson:
        keydict = json.load(keyjson)
        apikey = keydict["apikey"]
    return apikey

def search(query, type):
    params = {
        "key": f"{readKey()}",
        "part": "snippet",
        "maxResults": 5,
        "type": "video",
        "q": f"{query}"
    }

    searchres = requests.get(f"{googleapi}/search", params=params).content
    responsedicttmp = json.loads(codecs.decode(searchres))
    # print(codecs.decode(searchres))
    
    with open("/tmp/apiresponse.json", "w") as responsejsonfilew:
        json.dump(responsedicttmp, responsejsonfilew, indent=4)
 
    with open("/tmp/apiresponse.json", "r") as responsejsonfiler:
        responsejson = json.load(responsejsonfiler)
        fetchedvideosname = []
        fetchedvideosids = []

        for x in responsejson["items"]:
            fetchedvideosids.append(x["id"]["videoId"])
            fetchedvideosname.append(x["snippet"]["title"])

    if type == "ids":
        return fetchedvideosids
    elif type == "names":
        return fetchedvideosname
    else:
        pass
