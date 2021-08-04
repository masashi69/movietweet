import requests
import sys
import json
import configure
import re

KEY = configure.APIKEY
url = 'http://www.omdbapi.com/'
gettitle = '+'.join(sys.argv[1:])
getinfo = ''.join([url, '?apikey=', KEY, '&t=', gettitle])

def main():

	movieinfo = requests.get(getinfo)
	dataload = json.loads(movieinfo.text)

	datadump = json.dumps(dataload, indent=0)

	shapedata = re.sub('\n.\n|"|{|}|\[|\]', "", datadump)
	shapedata = re.sub(',\n', "\n", shapedata)

	print(shapedata)

if __name__ == '__main__':
	main()
