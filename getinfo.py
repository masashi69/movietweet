import requests
import sys
import json
import configure
import re
import argparse

KEY = configure.APIKEY
url = 'http://www.omdbapi.com/'

def getmovieinfo(infos):

	movieinfo = requests.get(infos)
	dataload = json.loads(movieinfo.text)

	datadump = json.dumps(dataload, indent=0)

	shapedata = re.sub('\n.\n|"|{|}|\[|\]', "", datadump)
	shapedata = re.sub(',\n', "\n", shapedata)

	return shapedata

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('--title', nargs='+', help='Input movie title', required=True)
	parser.add_argument('--year',type=int, help='Specify released year')
	args = parser.parse_args()

	gettitle = '+'.join(args.title)
	getinfo = ''.join([url, '?apikey=', KEY, '&t=', gettitle])

	if args.year:
		getinfo_y = ''.join([url, '?apikey=', KEY, '&t=', gettitle, '&y={}'.format(args.year)])
		i = getmovieinfo(getinfo_y)
	else:
		i = getmovieinfo(getinfo)

	print(i)

if __name__ == '__main__':
	main()
