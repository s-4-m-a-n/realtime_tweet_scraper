import json
import os

def load_json(json_file):
	if json_file not in os.listdir():
		return []
		
	with open(json_file,"r+") as f:
		json_obj = json.load(f)	
	return json_obj

def save_json(tweet_json_obj,json_file):
	#load json file if exists
	existing_tweet_json = load_json(json_file)
	
	#filter text that doesnot exist already in the json_obj
	#for tweet in existing_tweet_json:
	
	existing_tweet_json += tweet_json_obj #appending new tweet json obj to the existing tweet json obj
	
	#saving the json file
	
	with open(json_file,"w") as f:
		json.dump(existing_tweet_json,f)
	return ("tweet json is updated",len(existing_tweet_json)) 
		
