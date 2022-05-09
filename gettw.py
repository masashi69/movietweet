#!/usr/bin/env python3

from tweetapi import TWauth
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--year',type=int, help='Specify posted year')
args = parser.parse_args()

API = TWauth()

def find_title():
    Posted = info.created_at + datetime.timedelta(hours=9)
    Text = info.text[info.text.find('「')+1:info.text.find('」')]
    return Posted, Text

for i in range(1, 5):
    for info in API.user_timeline(count=200, page=i):
        if 'tweet movieinfo' in info.source:
            if args.year:
                post, text = find_title()
                if info.created_at.year == args.year:
                    print(post, text)
                else:
                    pass
            else:
                post, text = find_title()
                print(post, text)
        else:
            pass

