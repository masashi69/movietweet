#!/usr/bin/env python3

from tweetapi import TWauth
import sys

api = TWauth()

# ツイート
api.update_status(sys.argv[1])

