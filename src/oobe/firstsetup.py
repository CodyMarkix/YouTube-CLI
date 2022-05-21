import os
import json

def setup():
    apikeydict = {}
    apijsonpath = os.path.join(os.path.expanduser("~"), ".local", "share", "ytcli", "apikey.json")
    apikeyprompt = """Open your Google Cloud Platform Dashboard and create a new project.
Enable Youtube Data API v3 and add an API key.
Then paste the API key here: """
    
    os.makedirs(os.path.join(os.path.expanduser("~"), ".local", "share", "ytcli"))
    apikeyinpt = input(apikeyprompt)
    apikeydict.update({"apikey": f"{apikeyinpt}"})

    with open(apijsonpath, "w") as apijson:
        json.dump(apikeydict, apijson, indent=4)
