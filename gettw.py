#!/usr/bin/env python3

from tweetapi import TWauth
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--year',type=int, help='Specify posted year')
args = parser.parse_args()

API = TWauth()

def find_title(apis):
    Posted = apis.created_at + datetime.timedelta(hours=9)
    Text = apis.text[apis.text.find('「')+1:apis.text.find('」')]

    return Posted, Text

def get_timeline(maxid=None):
    timelines = API.user_timeline(count=200, max_id=maxid)

    return timelines

def main():

    movies_list = []
    maxid=None
    maxid_year = {2021: 1477970574488252416 ,2020: 1345640504269053952, \
                  2019: 1212178772645928960, 2018: 948490042174943233}

    if args.year:
        maxid = maxid_year.get(args.year)

    timelines = get_timeline(maxid)

    for i in range(3):

        maxid = timelines.max_id
        timelines += get_timeline(maxid)

    for info in timelines:
        if info.source == 'tweet movieinfo':
            post, text = find_title(info)
            if args.year:
                if info.created_at.year == args.year:
                    movies_list.append({'posted_date': post, 'title': text})
                else:
                    pass
            else:
                movies_list.append({'posted_date': post, 'title': text})
        else:
            pass


    return movies_list


if __name__ == '__main__':
    movies = main()
    for movie in movies:
        print(movie['posted_date'].strftime('%Y-%m-%d %H:%M:%S'), movie['title'])
