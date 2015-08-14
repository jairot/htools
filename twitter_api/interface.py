 # encoding=utf-8
import twitter
from os import path
from json import dumps

from .settings import (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY,
                       ACCESS_TOKEN_SECRET)


class TwitterInterface():

    def search_tweets(self, hashtag, since_id=0, count=15):
        try:
            api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
            # print api.VerifyCredentials()
            tweets = api.GetSearch(hashtag, since_id=since_id, count=count)
            if tweets:
                last_id = tweets[0].GetId()
            return dumps([x.AsJsonString() for x in tweets]), last_id if last_id else None
        except Exception as e:
            print e
            return dumps([]), None

    def get_user_profile(self, user_id):
        try:
            api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

            user_info = api.GetUser(user_id=user_id)
            return dumps(user_info)
        except Exception as e:
            print e
            return dumps([])
