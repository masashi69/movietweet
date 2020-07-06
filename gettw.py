#!/usr/bin/env python3

from tweetapi import TWauth
import datetime

API = TWauth()

for i in range(1, 5):
    for info in API.user_timeline(count=200, page=i):
        if 'tweet movieinfo' in info.source:
            Posted = info.created_at + datetime.timedelta(hours=9)
            Text = info.text[info.text.find('「')+1:info.text.find('」')]
            print(Posted, Text)
        else:
            pass

