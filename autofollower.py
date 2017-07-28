import tweepy
import time

auth = tweepy.OAuthHandler("IGhBIYxqhcXHXVqfj1ejxUyEs","OK0xmRUGAbiEYKYGytC93FYstYULhmkB1ACoeFgDnWM7yj1BST")
auth.set_access_token("889483743429353472-N3ubnWvAyHYDhq545N1tVmXy1juWPea","Ie5NAgWAodLdrS9J4Md2VcgdOAd6qgugx59h4zwi1VBOo")
api = tweepy.API(auth)

for follower in tweepy.Cursor(api.search, q="#PackersCamp").items():
    print(follower)
    api.create_friendship(follower.user.id)
