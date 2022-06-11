#!/usr/bin/env python3

import tweepy
import configure

Consumer_Key=configure.CK
Consumer_Secret=configure.CS
Access_Token=configure.AT
Access_Secret=configure.AS

def TWauth():
    auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
    auth.set_access_token(Access_Token, Access_Secret)
    api = tweepy.API(auth)

    return api

if __name__ == '__main__':
    TWauth()

