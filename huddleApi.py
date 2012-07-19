import oAuth
import token
import urllib2
import json

class huddleApi:
        def __init__(self,HuddleAuthServer,tokenStore):
            self.HuddleAuthServer = HuddleAuthServer
            self.tokenStore = tokenStore

        def getUser(self):
            proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8888'})  
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)

            headers = { 'Accept' : 'application/vnd.huddle.data+json', 'Authorization' : 'OAuth2'+self.tokenStore.getAccessToken()}
            uri = "http://api.huddle.dev/" + "entry/"
            req = urllib2.Request(uri, headers=headers )
            response = urllib2.urlopen(req)
            return response

        def getFolders(self,uri):
            headers = { 'Accept' : 'application/json', 'Authorization' : 'OAuth2'+self.tokenStore.getAccessToken()}
            print self.uri

        def deleteContent(self,uri):
            headers = { 'Accept' : 'application/json', 'Authorization' : 'OAuth2'+self.tokenStore.getAccessToken()}
            print self.uri

        def createFolder(self, name, desc, uri):
            headers = { 'Accept' : 'application/json', 'Authorization' : 'OAuth2'+self.tokenStore.getAccessToken()}
            body = "<folder title=" + name +  " description=" + desc + "/>"
            
            req = urllib2.Request(self.uri, body, headers)
            response = urllib2.urlopen(req)

            print response

        def createFile(self, name, desc, uri):
            headers = { 'Accept' : 'application/vnd.huddle.data+xml', 'Authorization' : 'OAuth2'+self.tokenStore.getAccessToken()}
            body = "<document title=" +  name +  " description=" + desc +  "/>"
            
            req = urllib2.Request(self.uri, body, headers)
            response = urllib2.urlopen(req)

            print response

        def uploadToFile(self, document, uri):
            headers = { 'Accept' : 'application/json', 'Authorization' : 'OAuth2'+self.tokenStore.getAccessToken()}
            print document + " " + self.uri
            
    
