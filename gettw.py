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

def main():

    movies_list = []

    for i in range(1, 5):
        for info in API.user_timeline(count=200, page=i):
            if 'tweet movieinfo' in info.source:
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
        print(movie['posted_date'].strftime('%Y/%m/%d %H:%M:%S'), movie['title'])
