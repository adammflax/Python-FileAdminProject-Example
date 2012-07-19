import oAuth
import huddleApi
import document
import os
import folder

huddleAuthServer = "http://login.huddle.dev/"
huddleApiServer = "http://api.huddle.dev/"
consumer_key = "FileAdminProjectHuddleOob"
redirect_uri = "urn:ietf:wg:oauth:2.0:oob"


def run_example():
    #first lets get the auth code from the client
    request_token_url = huddleAuthServer + "request?response_type=code" + "&client_id=" + consumer_key + "&redirect_uri=" + redirect_uri

    print "Get Your Authorization Code and paste it back into python\n" + request_token_url
    code = raw_input('--> ')

    auth = oAuth.oAuth(huddleAuthServer, code, consumer_key, redirect_uri)

    #store our access token
    tokenStore = auth.handleAccessToken()

    #now we can make calls to the api
    #we only have the uri for what folder we want to create the file in so first of all lets find the upload uri of that
    api = huddleApi.huddleApi(huddleApiServer, tokenStore)
    getFolder = folder.folder(api.getFolder("http://api.huddle.dev/files/folders/1237980/"))
    print getFolder.getLinksWithRel("create-document")
    getDocument = document.document(api.createFile("foo", "bar", getFolder.getLinksWithRel("create-document")))

    #time to upload the contents
    api.uploadToFile("C:\\Users\\adam.flax\\Documents\\foo.txt", getDocument.getLinkWithRel("upload"))
    os.system("pause")

if __name__ == '__main__':
    run_example()
    print 'Done.'
