from twitter_scraper import client
from twitter_scraper.scraper import get_tweets
from twitter_scraper.json_handler import save_json

#config--------------------------
JSON_FILE = "tweets repo/tweets.json"

def run(query="#motivationalquotes",max_results=10):
	#get tweety client 
	c = client.get_client()
	
	#get tweet
	tweets = get_tweets(c,query,max_results)
	print(tweets)
	#save tweet
	status = save_json(tweets,JSON_FILE)
	if status:
		print(f"{status[0]} \n {len(tweets)} tweets are added \n total tweets : {status[1]}")
	else:
		print("something went wrong")

if __name__ =="__main__":
	run()
