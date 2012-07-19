import oAuth
import huddleApi
import user
import os

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
    api = huddleApi.huddleApi(huddleApiServer, tokenStore)
    getWorkspaces = user.user(api.getUser())

    print "You currently have " + str(getWorkspaces.getWorkSpaceSize()) + " workspaces!"
    for i in range(getWorkspaces.getWorkSpaceSize()):
        print "\nWorkspace : " + str(getWorkspaces.getWorkSpaceTitle(i)) + " has the following links: "
        for x in range(getWorkspaces.getWorkSpaceLinks(i)):
            print getWorkspaces.getWorkSpaceLinkRel(i, x) + ":" + getWorkspaces.getWorkSpaceLinkHref(i, x)

    os.system("pause")

if __name__ == '__main__':
    run_example()
    print 'Done.'
