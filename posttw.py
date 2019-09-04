import tweepy
import sys
import configure

Consumer_Key=configure.CK
Consumer_Secret=configure.CS
Access_Token=configure.AT
Access_Secret=configure.AS

auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
auth.set_access_token(Access_Token, Access_Secret)
api = tweepy.API(auth)

# ツイート
api.update_status(sys.argv[1])

