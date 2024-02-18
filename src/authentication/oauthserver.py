from flask import Flask, request
import requests, json, os

class OAuthServer:
    app = None

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        pass

    def setClientID(self, clientID):
        self.client_id = clientID
        return self.client_id
    
    def setClientSecret(self, clientSecret):
        self.client_secret = clientSecret
        return self.client_secret

    def startServer(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/callback', view_func=self.callbackRoute)

        self.app.run(debug=False, port=8080)
    
    def callbackRoute(self):
        tokensReq = requests.post('https://oauth2.googleapis.com/token', params={
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": "http://127.0.0.1:8080/callback",
            "grant_type": "authorization_code",
            "code": request.args["code"]
        })

        tokens = json.loads(tokensReq.text)
        tokens.update({"client_id": self.client_id, "client_secret": self.client_secret})
        breakpoint()

        with open(os.path.join(os.path.expanduser("~"), ".local", "share", "ytcli", "OAuth2creds.json"), 'w') as f:
            json.dump(tokens, f)

        breakpoint()        
        return "You may now close this"