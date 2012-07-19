from datetime import datetime, timedelta

class Token:
    def __init__(self,Access_Token, Refresh_Token,Refresh_Time):
        self.Access_Token = Access_Token
        self.Refresh_Token = Refresh_Token
        self.Refresh_Time = Refresh_Time
        self.ExpiryTime = datetime.now() + timedelta (seconds=Refresh_Time)

    def getAccessToken(self):
        return self.Access_Token
    
    def getRefreshToken(self):
        return self.Refresh_Token
    
    def getRefreshTime(self):
        return self.Refresh_Time

    def isExpired(self):
        currentTime = datetime.now()
        if currentTime > self.ExpiryTime:
            return True
        else:
            return False
