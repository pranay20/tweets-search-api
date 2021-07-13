# Standard application imports
import os
import json
import datetime

# Django core imports
from django.conf import settings

# Third party imports
import pytz
import tweepy

# Local application imports
from .models import Tweet

TWEETS_PER_USER = 50

def fetch_tweets():

	def initialize_twitter_api():
		twitter_creds_path = getattr(settings, 'TWITTER_CREDS_PATH', '')
		twitter_creds = {}

		if os.path.exists(twitter_creds_path):
			with open(twitter_creds_path, 'r') as file:
				twitter_creds = json.load(file)

		if twitter_creds:
			api_key = twitter_creds.get("API_KEY")
			api_key_secret = twitter_creds.get("API_SECRET")
			access_token = twitter_creds.get("ACCESS_TOKEN")
			access_token_key = twitter_creds.get("ACCESS_TOKEN_SECRET")

			auth = tweepy.OAuthHandler(api_key, api_key_secret)
			auth.set_access_token(access_token, access_token_key)

			api = tweepy.API(auth)
			return api

	api = initialize_twitter_api()

	if not api:
		print("Twitter API not initialized. Please check if twitter creds file exists & creds are valid")
		return

	# delete existing tweets
	# Tweet.delete_all()

	usernames = getattr(settings, 'TWITTER_USERNAMES', [])
	user_tweets = []
	for username in usernames:
		print(f"fetching tweets for user: @{username}")
		result = tweepy.Cursor(
					api.user_timeline,
					id=username,
					tweet_mode="extended"
				).items(TWEETS_PER_USER)

		for tweet in result:
			user = tweet.user
			text = tweet.full_text
			created_at = tweet.created_at

			text = text.encode('utf-8').decode('utf-8')

			# add timezone to date time
			created_at = created_at.replace(tzinfo=pytz.timezone("UTC"))

			tweet_data = {
				"text": text,
				"username": f"@{username}",
				"created_at": created_at
			}
			# create a tweet in db
			Tweet.create(tweet_data)

			user_tweets.append(tweet_data)

	return user_tweets