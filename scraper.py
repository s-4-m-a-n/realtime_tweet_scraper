import tweepy
from client import get_client
import re

def is_tag(string):
    tag_pattern = "#[A-Z|0-9|_]*"
    return bool(re.match(tag_pattern,string))

#not working as expected    
def has_link(string):
    link_pattern = ".*[https:].*.com"
    return bool(re.match(link_pattern,string))

def parse_text(text):
    """return the clean text and hashtags separately"""
    pattern = "([^#]*)(#.*)"
    match = re.search(pattern,text)
    text = match.group(1)
    tags = match.group(2).split(" ")

    #removing other thing from the tags
    filtered_tags = []
    for tag in tags:
        if is_tag(tag):
            filtered_tags.append(tag)
    
    return {"text":text,"tags":filtered_tags}


def get_tweets(client,query="hello", max_results=10):
    tweets = client.search_recent_tweets(query)
    response = []
    if tweets.data:
    	for tweet in tweets.data:
        	if "@" in tweet.text:
        		continue;
        	response.append({"id":tweet.id,"tweet":parse_text(tweet.text)})
    
    return response
    
    
    
if __name__ == "__main__":
	client = get_client()
	
	print(get_tweets(client=client,query="#motivationalquotes",max_results=10))

