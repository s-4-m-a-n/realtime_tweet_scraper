
# Without Docker
* create virtual env
	 ``` python3 -m venv <myEnv>```
* activate virtual env
	``` source <myEnv>/bin/activate```
* install all the dependencies from requirements.txt
      ``` pip install -r requirements.txt```
* add environmental variables
	``` source env.sh ```
* run 
``` python3 tweet_scraper/worker.py```

>>> Note: twitter_scraper->worker.run runs the script and stores the result in the tweets repo
