import oAuth
import time
import huddleApi
import token
import user

huddleAuthServer = "http://login.huddle.dev/"
huddleApiServer = "http://api.huddle.dev/"
consumer_key = "FileAdminProjectHuddleOob"
redirect_uri = "urn:ietf:wg:oauth:2.0:oob"

def run_example():
    #first lets get the auth code from the client
    request_token_url = huddleAuthServer + "request?response_type=code" + "&client_id=" + consumer_key + "&redirect_uri=" + redirect_uri
                                                                                                          
    print "Get Your Authorization Code and paste it back into python\n" + request_token_url
   # code =raw_input('--> ')
    code = "99a63a4a-b0aa-4720-9b58-9e09e038e941"
    
    auth = oAuth.oAuth(huddleAuthServer,code,consumer_key,redirect_uri)
    tokenStore = auth.handleAccessToken() #store our access token

    #now we can make calls to the api
    api = huddleApi.huddleApi(huddleApiServer, tokenStore)
    getWorkspaces = user.user(api.getUser())

    print getWorkspaces.getWorkSpaceTitle(0)
    print getWorkspaces.getWorkSpaceLinkRel(0,0)

if __name__ == '__main__':
    run_example()
    print 'Done.'

    
