import requests
import codecs
import json
import os

googleapi = "https://www.googleapis.com/youtube/v3"
jsonpath = os.path.join(os.path.expanduser("~"), ".local", "share", "ytcli", "OAuth2Creds.json")

def __readAccessToken():
    with open(jsonpath, 'r') as keyjson:
        jsonData = keyjson.read()
        keydict = json.loads(jsonData)
        apikey = keydict["access_token"]

    return apikey

def search(query, type, searchtype):
    params = {
        "part": "snippet",
        "maxResults": 5,
        "type": f"{searchtype}",
        "q": f"{query}"
    }

    headers = {
        "Authorization": f"Bearer {__readAccessToken()}"
    }

    searchres = requests.get(f"{googleapi}/search", params=params, headers=headers).content
    responsedicttmp = json.loads(codecs.decode(searchres))
    # print(codecs.decode(searchres))
    
    apiResonseFile = f"{os.environ['USERPROFILE']}\\AppData\\Local\\Tempapiresponse.json" if os.name == 'nt' else "/tmp/Tempapiresponse.json"

    with open(apiResonseFile, "w") as responsejsonfilew:
        json.dump(responsedicttmp, responsejsonfilew, indent=4)


    if searchtype == "video":
        with open(apiResonseFile, "r") as responsejsonfiler:
            responsejson = json.load(responsejsonfiler)
            fetchedvideosname = []
            fetchedvideosids = []

            for x in responsejson["items"]:
                fetchedvideosids.append(x["id"]["videoId"])
                fetchedvideosname.append(x["snippet"]["title"])

    elif searchtype == "playlist":
        pass

    if type == "ids":
        return fetchedvideosids
    elif type == "names":
        return fetchedvideosname

def fetchVideoInfo(videoId: str):
    params = {
        "part": "snippet,replies",
        "videoId": videoId,
        "maxResults": "5"
    }

    headers = {
        "Authorization": f"Bearer {__readAccessToken()}"
    }

    req = requests.get(f"{googleapi}/commentThreads", params=params, headers=headers)
    with open("outAPI.json", "wb") as f:
        f.write(req.content)

    return json.loads(req.text)