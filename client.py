import tweepy
import configparser

#-----config--------------------------------------------
#read config
CONFIG_FILE = "config.ini"
config = configparser.ConfigParser()
config.read(CONFIG_FILE)

#getting api key and token from configparser obj
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
bearer_token = config['twitter']['bearer_token']


def get_client():
	client = tweepy.Client(bearer_token=bearer_token,
				consumer_key=api_key,
				consumer_secret=api_key_secret,
				access_token=access_token,
				access_token_secret=access_token_secret)
				
	return client


