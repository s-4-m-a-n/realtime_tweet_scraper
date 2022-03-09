import tweepy
import configparser

#-----config--------------------------------------------
#read config
CONFIG_FILE = "config.ini"

api_key = "ULlWIqWGtgoRpcSaoFXOFH7yk"
api_key_secret = "4O1KEfHshUMKeX3MWRtSv8YFp9SBpGJ3hNjJQ2PPdOcgmFYc7g"

access_token = "1501180343424262144-tMJmQYAdjTICrosJFrLL0GYG1BSNFh"
access_token_secret = "xUXwGJABhOJNeOQsr3LmYGQg7WI42GFA3VJRhUBxkXqLT"
bearer_token ="AAAAAAAAAAAAAAAAAAAAAO8EaAEAAAAAt4yKRin9eDbP56x2tA2k3c9oN6Y%3DLIj5n3lkGQYO5O7NSEr224ee1ttZHghhw4yFwQU3ZGhQtdZB0Q"



def get_client():
	config = configparser.ConfigParser()
	config.read(CONFIG_FILE)
	
	#getting api key and token from configparser obj
	#api_key = config['twitter']['api_key']
	#api_key_secret = config['twitter']['api_key_secret']
	#access_token = config['twitter']['access_token']
	#access_token_secret = config['twitter']['access_token_secret']
	#bearer_token = config['twitter']['bearer_token']
	client = tweepy.Client(bearer_token=bearer_token,
				consumer_key=api_key,
				consumer_secret=api_key_secret,
				access_token=access_token,
				access_token_secret=access_token_secret)
				
	return client


