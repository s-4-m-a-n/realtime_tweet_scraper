import tweepy
import configparser
import os
#-----config--------------------------------------------
#read config
CONFIG_FILE = "config.ini"

credientials= {
	'consumer_key' : os.environ['API_KEY'],
	'consumer_secret' : os.environ['API_KEY_SECRET'],

	'access_token' : os.environ['ACCESS_TOKEN'],
	'access_token_secret' : os.environ['ACCESS_TOKEN_SECRET'],
	'bearer_token' : os.environ['BEARER_TOKEN']
} 


def get_client():
	config = configparser.ConfigParser()
	config.read(CONFIG_FILE)
	
	#getting api key and token from configparser obj
	#api_key = config['twitter']['api_key']
	#api_key_secret = config['twitter']['api_key_secret']
	#access_token = config['twitter']['access_token']
	#access_token_secret = config['twitter']['access_token_secret']
	#bearer_token = config['twitter']['bearer_token']
	client = tweepy.Client(**credientials)
				
	return client


