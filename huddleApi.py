import oAuth
import token
import urllib2
import json
from poster.encode import multipart_encode  # You can find the lib at: http://pypi.python.org/pypi/poster/0.4
from poster.streaminghttp import register_openers


class huddleApi:
        def __init__(self, HuddleAuthServer, tokenStore):
            self.HuddleAuthServer = HuddleAuthServer
            self.tokenStore = tokenStore

        def getUser(self):
            headers = {'Accept': 'application/vnd.huddle.data+json', 'Authorization': 'OAuth2' + self.tokenStore.getAccessToken()}
            uri = "http://api.huddle.dev/" + "entry/"
            req = urllib2.Request(uri, headers=headers)
            response = urllib2.urlopen(req)
            return response

        def getFolder(self, uri):
            headers = {'Accept': 'application/vnd.huddle.data+json', 'Authorization': 'OAuth2' + self.tokenStore.getAccessToken()}
            req = urllib2.Request(uri, headers=headers)
            response = urllib2.urlopen(req)
            return response

        def createFile(self, name, desc, uri):
            headers = {'Accept': 'application/vnd.huddle.data+json', 'Authorization': 'OAuth2 ' + self.tokenStore.getAccessToken(), 'Content-Type': 'application/json'}
            body = "{title:" + "\"" + name + "\"" + " ,description:" + "\"" + desc + "\"" + "}"

            req = urllib2.Request(uri, body, headers)
            response = urllib2.urlopen(req)

            return response

        def uploadToFile(self, document, uri):
            register_openers()
            values = {'filename': open(document)}
            data, headers = multipart_encode(values)
            #add our headers
            headers['Authorization'] = 'OAuth2 ' + self.tokenStore.getAccessToken()

            request = urllib2.Request(uri, data, headers)
            request.unverifiable = True
            urllib2.urlopen(request)
