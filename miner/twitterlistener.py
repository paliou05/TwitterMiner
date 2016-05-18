import json
import datetime
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from .models import User

ckey=""
csecret=""
atoken=""
asecret=""

class listener(StreamListener):
    
    def on_data(self, data):
        try:
            user = User()
            json_data = json.loads(data)
            user.name = json_data['user']['name']
            user.tweet = json_data['text']
            user.followers = json_data['user']['followers_count']
            user.favourited = json_data['user']['favourites_count']
            user.retweets = json_data['retweet_count']
            user.screen_name = json_data['user']['screen_name']
            user.description = json_data['user']['description']
            user.save()
            
            print user.description.encode('utf8')

        except BaseException,e:
            user.description = ""
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

    
    