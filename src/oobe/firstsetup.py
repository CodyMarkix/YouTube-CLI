import os, time
import json, sys
from multiprocessing import Process

def setup(OAuthServer):
    apijsonpath = os.path.join(os.path.expanduser("~"), ".local", "share", "ytcli", "oauth2.json")
    oauth2prompt = """Open your Google Cloud Platform Dashboard and create a new project.
Enable Youtube Data API v3 and create an OAuth2 client.
Download the clientID json and paste the filepath here: """
    
    try:
        os.makedirs(os.path.join(os.path.expanduser("~"), ".local", "share", "ytcli"))
    except FileExistsError:
        print("[INFO] ytcli config folder exists")

    apikeyinpt = input(oauth2prompt)
    
    with open(apikeyinpt, 'r') as credsFile:
        credentials = json.load(credsFile)["installed"]

        OAuthServer.client_id = credentials["client_id"]
        OAuthServer.client_secret = credentials["client_secret"]
    
    scopes = "https://www.googleapis.com/auth/youtube%20https://www.googleapis.com/auth/youtube.force-ssl"

    input(f"\nGo to \033[1mhttps://accounts.google.com/o/oauth2/auth?client_id={credentials['client_id']}&scope={scopes}&redirect_uri=http://127.0.0.1:8080/callback&response_type=code\033[0m and sign in via your Google account. Press enter to start the authentication process and Ctrl+C when you finish signing in. ")
    
    print("[INFO] Starting server")
    OAuthServer.startServer()

    print("\n[INFO] OAuth2 credentials saved")
    print("Please restart the app now.")
    sys.exit(0)
