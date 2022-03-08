from client import get_client
from scraper import get_tweets
from json_handler import save_json

#config--------------------------
JSON_FILE = "tweets.json"

def run():
	#get tweety client 
	client = get_client()
	
	#get tweet
	tweets = get_tweets(client=client,query="#motivationalquotes",max_results=10)
	
	#save tweet
	status = save_json(tweets,JSON_FILE)
	if status:
		print(f"{status[0]} \n {len(tweets)} tweets are added \n total tweets : {status[1]}")
	else:
		print("something went wrong")

if __name__ =="__main__":
	run()
