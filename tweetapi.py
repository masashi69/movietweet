#!/usr/bin/env python3

import tweepy
import configure

Bearer_Token=configure.BA
Consumer_Key=configure.CK
Consumer_Secret=configure.CS
Access_Token=configure.AT
Access_Secret=configure.AS

def TWauth():
    api = tweepy.Client(bearer_token=Bearer_Token, consumer_key=Consumer_Key, consumer_secret=Consumer_Secret, access_token=Access_Token, access_token_secret=Access_Secret)

    return api

TWauth()

