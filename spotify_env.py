from dotenv import load_dotenv
import os
import base64
from requests import post
import json

# get env file 
load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
# print( client_id, client_secret )
class Spotify:
    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")

    def get_token(self):
        auth_string = self.client_id + ':' + self.client_secret
        auth_byte = auth_string.encode("utf-8")
        auth_base4 = str(base64.b64encode(auth_byte), "utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic "+ auth_base4,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}
        result = post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        token = json_result["access_token"]
        return token

    def get_auth_header(self):
        token = self.get_token()
        return {"Authorization": "Bearer " + token}