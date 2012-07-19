import json

#instead store each workspace as a seperate dict
class user:
    def __init__(self, jsonBlob):
        self.jsonBlob = jsonBlob
        self.jsonParse = json.load(self.jsonBlob)

    def getWorkSpaceTitle(self, workspaceId):
        print self.jsonParse['membership']['workspaces'][workspaceId]['title']

    def getWorkSpaceType(self, workspaceId):
        print self.jsonParser['membership']['workspaces'][workspaceId]['type']

    def getWorkSpaceSettingsName(self, workspaceId, settingId):
        print self.jsonParse['membership']['workspaces'][workspaceId]['settings'][settingId]['name']
        
    def getWorkSpaceSettingsValue(self, workspaceId):
        print self.jsonParse['membership']['workspaces'][workspaceId]['settings'][settingId]['value']
        
    def getWorkSpaceLinkHref(self, workspaceId, linkId):
        print self.jsonParse['membership']['workspaces'][workspaceId]['links'][linkId]['href']
        
    def getWorkSpaceLinkRel(self, workspaceId, linkId):
        print self.jsonParse['membership']['workspaces'][workspaceId]['links'][linkId]['rel']
        
