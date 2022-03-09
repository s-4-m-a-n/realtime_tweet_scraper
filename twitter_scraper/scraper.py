import tweepy
from twitter_scraper.client import get_client
import re
import hashlib


def is_tag(string):
    tag_pattern = "#[A-Z|0-9|_]*"
    return bool(re.match(tag_pattern,string))

   
def has_url(string):
    url_pattern = "http[s]{0,1}:"
    return bool(re.search(url_pattern,string))

def normalize_text(string):
    noise_pattern = "[^a-zA-Z0-9-_'\"+ ]"
    filtered_string = re.sub(noise_pattern,"",string)
    #remove multiple whitespaces
    filtered_string = " ".join(filtered_string.split())
    #lower case
    filtered_string = filtered_string.lower()
    return filtered_string

def hash_fn(text):
    encoded = text.encode()
    result = hashlib.sha256(encoded)
    return result.hexdigest()

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
    tweets = client.search_recent_tweets(query=query, max_results=max_results)
    response = {}
    if tweets.data:
        for tweet in tweets[0]:
            if "@" in tweet.text or has_url(tweet.text) or len(tweet.text) < 5: #discard tweet that has mentions and urls
                continue;
            parsed_text = parse_text(tweet.text)
            tweet_text = normalize_text(parsed_text["text"])
            tweet_hash = hash_fn(tweet_text)
            response[tweet_hash] = {"text":tweet_text,"tags":parsed_text["tags"]}      
    return response
    
    
    
if __name__ == "__main__":
	c = get_client()
	
	print(get_tweets(client=c,query="#motivationalquotes",max_results=10))

