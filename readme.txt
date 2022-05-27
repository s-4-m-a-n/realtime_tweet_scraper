# twitter_scraper worker.run runs the script and stores the result in the tweets repo


#to execute the fetching process
python3 worker.py


# Without Docker
* create virtual env
	 ``` python3 -m venv <myEnv>```
* install all the dependencies from requirements.txt
      ``` pip install -r requirements.txt```
* add environmental variables
	``` source env.sh ```
* run 
``` python3 tweet_scraper/worker.py```
