#!/usr/bin/env python3

from tweetapi import TWauth
import datetime

for info in TWauth().user_timeline(count=200):
    if 'tweet movieinfo' in info.source:
        Posted = info.created_at + datetime.timedelta(hours=9)
        Text = info.text[info.text.find('「')+1:info.text.find('」')]
        print(Posted, Text)
    else:
        pass

