import client
from scraper import get_tweets
from json_handler import save_json




def run(query="#quotes",max_results=50):
	# config 
	JSON_FILE = f"tweets repo/{query[1:]}.json"
	
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
