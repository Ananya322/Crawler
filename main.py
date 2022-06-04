import queue
import threading
from queue import Queue

# each thread(spider) does it own task(queue)
from spider import Spider
from domain import *
from crawler_1 import *

Project_name = 'Vulnerability Scanner'  # variable -> not going to change
Homepage = 'https://hackerone.com/duckduckgo?type=team'
# Homepage = input('Homepage URL:')
# print(Homepage)
Domainname = get_domainname(Homepage)
Queuefile = Project_name + '/queue.txt'
Crawledfile = Project_name + '/crawled.txt'
thread_number = 4
# thread_number = input("Number of spiders according to the OS:")
# print(thread_number)

# thread queue
queue = Queue()

# we cannot initiate a multi-threaded program at start first we need initial files
Spider(Project_name, Homepage, Domainname)


# create spiders,i.e., worker threads which end when main file exits the program
def createspiders():
    for _ in range(thread_number):
        # doesn't really matter here what the variable is we'll just run the loop n times because of which we use _
        thread = threading.Thread(target=work)
        thread.daemon = True
        # to exit the program as soon as the main program exits the functioning
        thread.start()


# Giving next task in queue to spider to do
def work():
    while True:
        url = queue.get()
        Spider.crawlpage(threading.current_thread().name, url)
        # current_thread is a built in python module which gives user the info of current thread file
        queue.task_done()


# check if there are links in queue. if yes then crawl them
def crawl():
    queued_links = file_to_set(Queuefile)
    if len(queued_links) > 0:
        print('Links queued:' + str(len(queued_links)))
        createtasks()


# each queue link is a new task
def createtasks():
    for url in file_to_set(Queuefile):
        queue.put(url)  # sticking the links in thread queue
    queue.join()  # to prevent various threads doing things all at once
    crawl()


createspiders()
crawl()

# to call spider again and again for a multi threaded program
# creating jobs for spiders(threads)
