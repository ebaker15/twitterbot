
import tweepy, time, sys, random
from random import randint

argfile = str("liners.txt")



#enter the corresponding information from your Twitter application:
CONSUMER_KEY =  '3e71WF8gjkJQZ9TuNMsj1XUtE'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'ybqQXb5Y4auL2Twyq7wpO6jbPVy7ajUQWV6quntW53EJuIQtXn'
ACCESS_KEY = '889483743429353472-T39k8ohUxOY6AZeptZ3JWzQCGaW1dK7'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'sLNkTKyg9dH3TiPgq1YShQRtMUfluWG9JBo5dBxH3tNJc'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

while True:
    for line in f:
        curtime= time.strftime("%H:%M:%S")
        curdate= time.strftime("%x")
        api.update_status("{0}---{1}, {2}".format(curdate,curtime,line))
        TimeToSleep = randint(780,1200)
        time.sleep(TimeToSleep)#Tweet every 15 minutes
