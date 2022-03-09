from redis import Redis
from rq import Queue
from rq_scheduler import Scheduler
from datetime import timedelta
import time
from twitter_scraper.worker import run


def main():
	
	#print("inside main")
	#queue = Queue(connection=Redis(host="redis_alp",port=6379))

	#print("connection established")
	#count = 10
	#try:
	#	print("inside try")
	#	while count > 0 :
	#		job = queue.enqueue(run,"#motivationalquotes")
	#		q_len = len(queue)
	#		print(f"Task : {job.id} \n added at: {job.enqueued_at} \n Queue size: {q_len}")
	#		time.sleep(10)
	#		print("hello")
	#		count -= 1
	#except Exception as e:
	#	print("something went wrong {}".format(e))
	run(max_results=50)

main()
	
