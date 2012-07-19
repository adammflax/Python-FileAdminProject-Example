import json
class document:
    def __init__(self, jsonBlob):
        self.jsonBlob = jsonBlob
        self.jsonParse = json.load(self.jsonBlob)

    def getdocumentLinks(self):
        return len(self.jsonParse['links'])

    def getdocumentLinksHref(self,  linkId):
        return self.jsonParse['links'][linkId]['href']

    def getdocumentLinksRel(self, linkId):
        return self.jsonParse['links'][linkId]['rel']

    def getLinkWithRel(self, Rel):
        for x in range(self.getdocumentLinks()):
            if self.jsonParse['links'][x]['rel'] == Rel:
                return self.jsonParse['links'][x]['href']
        return None

    def getLinkWithHref(self, Href):
        for x in range(self.getdocumentLinks()):
            if self.jsonParse['links'][x]['href'] == Href:
                return self.jsonParse['links'][x]['rel']
        return None
        
