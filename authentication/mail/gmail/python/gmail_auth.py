# import
import json
from apiclient.discovery import build
import webbrowser
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
# from oauth2client.tools import run
import httplib2
from apiclient import errors

# key_path
key_path = "key/"

# -
auth_url = "https://accounts.google.com/o/oauth2/auth?"

response_setting = {
    "scope": "https://mail.google.com/",
    "response_type": "code",
}

# -
f = open(key_path + "client_secret.json")
auth_info = json.load(f)


# -
class GoogleSomeApi:
    def __init__(self, auth_info):
        self.auth_info = auth_info
        self.service = GoogleServiceFactory().createService(self.auth_info)

    def reconnect(self):
        try:
            self.service = GoogleServiceFactory().createService(self.auth_info)
        except errors.HttpError as error:
            pass


# -
class GoogleServiceFactory:

    def createService(self, auth_info):
        STORAGE = Storage(key_path+'gmail.auth.storage')
        credent = STORAGE.get()
        if credent is None or credent.invalid:
            info = auth_info['installed']
            flow = OAuth2WebServerFlow(
                info["client_id"], 
                info["client_secret"], 
                response_setting["scope"], 
                info["redirect_uris"][0])
            auth_url = flow.step1_get_authorize_url()
            webbrowser.open(auth_url)
            code = input("input code : ")
            credent = flow.step2_exchange(code)
            STORAGE.put(credent)
        http = httplib2.Http()
        http = credent.authorize(http)

        google_some_service = build("gmail", "v1", http=http)
        return google_some_service


gmailApi = GoogleSomeApi(auth_info)




