import urllib2
import json
import token

class oAuth:
    def __init__(self,huddleAuthServer,code,consumer_key, redirect_uri):
        self.huddleAuthServer = huddleAuthServer
        self.code = code
        self.consumer_key = consumer_key
        self.redirect_uri = redirect_uri
        self.tokenStore = None

    def handleAccessToken(self):
        if self.tokenStore == None:
            return self.getAccessToken()
        if self.tokenStore.isExpired() == True:
            return self.getRefreshToken()
        else:
            return self.tokenStore
        

    def getAccessToken(self):
        headers = {"Accept": "application/json"}
        body = "grant_type=authorization_code&client_id=" + self.consumer_key + "&redirect_uri=" + self.redirect_uri + "&code=" + self.code
        url = self.huddleAuthServer + "token/"

        req = urllib2.Request(url, body, headers)
        response = urllib2.urlopen(req)
        jsonParse = json.load(response)
        self.tokenStore = token.Token(jsonParse['access_token'],jsonParse['refresh_token'],jsonParse['expires_in'])
        return self.tokenStore

    def getRefreshToken(self):
        headers = {"Accept": "application/json"}
        body = "grant_type=refresh_token&client_id=" + self.consumer_key + "&refresh_token=" +self.tokenStore.getRefreshToken()
        url = self.huddleAuthServer + "refresh/"

        req = urllib2.Request(url, body, headers)
        response = urllib2.urlopen(req)
        jsonParse = json.load(response)
        self.tokenStore = token.Token(jsonParse['access_token'],jsonParse['refresh_token'],jsonParse['expires_in'])
        return self.tokenStore

    

      

    
