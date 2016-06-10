import json
import datetime
import time
import urllib
from requests import *
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from .models import User, Tweet


ckey="KKwsfmkUMpv8ag7ptJPui5Xp8"
csecret="w6Fx0fPl7rfNayZXPgQ3crIAsWaNaENmtQJZJSnGgLJtoWs1Wt"
atoken="4178185372-Eq4HWoHZtOu1e8uizQhvEKF8ylRAqmBAf7zN2LK"
asecret="cC7RTyjoeQr68zAd1Dq6lhtnwAUO6AUQO2GUZow8EdKBC"

class listener(StreamListener):
    
    def on_data(self, data):
        try:
            user = User()
            json_data = json.loads(data)
            user.name = json_data['user']['name']
            user.friends = json_data['user']['friends_count']
            user.screen_name = json_data['user']['screen_name']
            user.followers = json_data['user']['followers_count']
            if user.friends == 0:
                user.trust = 0
            else:
                x=float(user.followers)
                y=float(user.friends)
                user.trust = x/y
            user.save()
            tweet = Tweet()
            tweet.user = user
            tweet.text = json_data['text']
            tweet.favourited = json_data['user']['favourites_count']
            tweet.retweets = json_data['retweet_count']
            tweet.description = json_data['user']['description']
            tweet.save()
            
            print tweet.description.encode('utf8')

        except BaseException,e:
            tweet.description = ""
            print "#################################"
            print "#### ADDED BLANK DESCRIPTION ####"
            print "#################################"
            time.sleep(5)
        return True
    
    def on_error(self, status):
        print status


def retrieve_data():
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=["rumor","claim"])

    
    