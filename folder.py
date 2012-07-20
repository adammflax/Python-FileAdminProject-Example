import json


class folder:
    def __init__(self, jsonBlob):
        self.jsonBlob = jsonBlob
        self.jsonParse = json.load(self.jsonBlob)

    def getLinks(self):
        return len(self.jsonParse['links'])

    def getLinksWithRel(self, rel):
        for x in range(self.getLinks()):
            if self.jsonParse['links'][x]['rel'] == rel:
                return self.jsonParse['links'][x]['href']
        return None

    def getLinksWithHref(self, href):
        for x in range(self.getLinks()):
            if self.jsonParse['links'][x]['href'] == href:
                return self.jsonParse['links'][x]['rel']
        return None

    def getFolderLinks(self, folderId):
        return len(self.jsonParse['folders'][folderId]['links'])

    def geFolderTitle(self, folderId):
        return self.jsonParse['folders'][folderId]['title']

    def getFolderUpdated(self, folderId):
        return self.jsonParse['folders'][folderId]['updated']

    def getFolderCreated(self, folderId):
        return self.jsonParse['folders'][folderId]['created']

    def getFolderDescription(self, folderId):
        return self.jsonParse['folders'][folderId]['description']

    def getFolderLinksHref(self, folderId, linkId):
        return self.jsonParse['folders'][folderId]['links'][linkId]['href']

    def getFolderLinksRel(self, folderId, linkId):
        return self.jsonParse['folders'][folderId]['links'][linkId]['rel']

    def getFolderLinkWithRel(self, folderId, Rel):
        for x in range(self.getFolderLinks(folderId)):
            if self.jsonParse['folders'][folderId]['links'][x]['rel'] == Rel:
                return self.jsonParse['folders'][folderId]['links'][x]['rel']
        return None

    def getFolderLinkWithHref(self, folderId, Href):
        for x in range(self.getFolderLinks(folderId)):
            if self.jsonParse['folders'][folderId]['links'][x]['href'] == Href:
                return self.jsonParse['folders'][folderId]['links'][x]['href']
        return None
