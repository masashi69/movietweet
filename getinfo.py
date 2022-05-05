import requests
import sys
import json
import configure
import re
import argparse

KEY = configure.APIKEY
url = 'http://www.omdbapi.com/'

parser = argparse.ArgumentParser()
parser.add_argument('--title', nargs='+', help='Input movie title', required=True)
parser.add_argument('--year',type=int, help='Specify released year')
args = parser.parse_args()

gettitle = '+'.join(args.title)
getinfo = ''.join([url, '?apikey=', KEY, '&t=', gettitle])

def getmovieinfo(infos=getinfo):

	movieinfo = requests.get(infos)
	dataload = json.loads(movieinfo.text)

	datadump = json.dumps(dataload, indent=0)

	shapedata = re.sub('\n.\n|"|{|}|\[|\]', "", datadump)
	shapedata = re.sub(',\n', "\n", shapedata)

	print(shapedata)

def main():

	if args.year:
		getinfo_y = ''.join([url, '?apikey=', KEY, '&t=', gettitle, '&y={}'.format(args.year)])
		getmovieinfo(getinfo_y)
	else:
		getmovieinfo()

if __name__ == '__main__':
	main()
