import json

#instead store each workspace as a seperate dict
class user:
    def __init__(self, jsonBlob):
        self.jsonBlob = jsonBlob
        self.jsonParse = json.load(self.jsonBlob)

    def getWorkSpaceSize(self):
        return len(self.jsonParse['membership']['workspaces'])

    def getWorkSpaceLinks(self, workspaceId):
        return len(self.jsonParse['membership']['workspaces'][workspaceId]['links'])

    def getWorkSpaceTitle(self, workspaceId):
        return self.jsonParse['membership']['workspaces'][workspaceId]['title']

    def getWorkSpaceType(self, workspaceId):
        return self.jsonParser['membership']['workspaces'][workspaceId]['type']

    def getWorkSpaceSettingsName(self, workspaceId, settingId):
        return self.jsonParse['membership']['workspaces'][workspaceId]['settings'][settingId]['name']
        
    def getWorkSpaceSettingsValue(self, workspaceId):
        return self.jsonParse['membership']['workspaces'][workspaceId]['settings'][settingId]['value']
        
    def getWorkSpaceLinkHref(self, workspaceId, linkId):
        return self.jsonParse['membership']['workspaces'][workspaceId]['links'][linkId]['href']
        
    def getWorkSpaceLinkRel(self, workspaceId, linkId):
        return self.jsonParse['membership']['workspaces'][workspaceId]['links'][linkId]['rel']
        
