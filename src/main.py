#!/usr/bin/env python3
import frontend
import oobe
import os, sys
import requests, json
from authentication import oauthserver

def main():
    if os.path.isfile(os.path.join(os.path.expanduser("~"), ".local", "share", "ytcli", "OAuth2Creds.json")):
        with open(os.path.join(os.path.expanduser("~"), ".local", "share", "ytcli", "OAuth2Creds.json"), 'r') as f:
            jsonData = f.read()
            cfg = json.loads(jsonData)
            cid = cfg["client_id"]
            csc = cfg["client_secret"]
            rt = cfg["refresh_token"]

        with open(os.path.join(os.path.expanduser("~"), ".local", "share", "ytcli", "OAuth2Creds.json"), 'w') as f:

            req = requests.post("https://oauth2.googleapis.com/token", params={
                "client_id": cid,
                "client_secret": csc,
                "refresh_token": rt,
                "grant_type": "refresh_token"
            })

            newToken = json.loads(req.text)
            newToken.update({"refresh_token": rt, "client_id": cid, "client_secret": csc})
            json.dump(newToken, f)

        frontend.menus.enterMenu()
    else:
        server = oauthserver.OAuthServer("", "")
        oobe.firstsetup.setup(server)

main()