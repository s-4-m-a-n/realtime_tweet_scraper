from redis import Redis
from rq import Queue
from rq_scheduler import Scheduler
from datetime import timedelta,datetime
import time
from twitter_scraper.worker import run
from test import show_msg

#def main():
	
#	print("inside main")
#	queue = Queue(connection=Redis(host="redis_alp",port=6379))

#	print("connection established")
#	count = 10
#	try:
#		print("inside try")
#		while count > 0 :
#			job = queue.enqueue(run,"#motivationalquotes")
#			q_len = len(queue)
#			print(f"Task : {job.id} \n added at: {job.enqueued_at} \n Queue size: {q_len}")
#			time.sleep(10)
#			print("hello")
#			count -= 1
#	except Exception as e:
#		print("something went wrong {}".format(e))
	#run(max_results=50)

def main():
	redis = Redis(host="redis_alp",port=6379)
	redis.flushdb()
	scheduler = Scheduler(connection=redis) # Get a scheduler for the "default" queue
	#queue.enque()
	print("connected")
	
	scheduler.enqueue_in(timedelta(minutes=1),show_msg)
	
	msg = scheduler.schedule(
    	scheduled_time=datetime.utcnow(), # Time for first execution, in UTC timezone
    	func=show_msg,                     # Function to be queued
    	#args=["#motivationalQuotes",10],             # Arguments passed into function when executed
    	interval=10,                   # Time before the function is called again, in seconds
    	repeat=10,                     # Repeat this number of times (None means repeat forever)
    	
	)
	if msg in scheduler:
		print("on scheduler")
	
	print(msg)
	print(len(list(scheduler.get_jobs())))
	print("scheduler count",scheduler.count())
	#while True:
	#	print(scheduler.get_jobs())
	#	time.sleep(60)
	print("exit")

main()
	
