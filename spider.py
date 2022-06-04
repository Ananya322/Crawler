from urllib.request import urlopen
from findlinks import LinkFinder
from crawler_1 import *


# urllib returns HTML code in binary format,i.e, bytes not human readable format
class Spider:
    # class variables are shared among all instances
    projectname = ''
    base_url = ''
    domainname = ''
    # variables for crawled and queued files txt files
    queuefile = ''
    crawledfile = ''
    # sets for queued and crawled files stored on RAM and are faster
    queue = set()
    crawled = set()

    def __init__(self, projectname, base_url, domainname):

        # for all spiders have same shared information

        Spider.projectname = projectname
        Spider.base_url = base_url
        Spider.domainname = domainname

        # set file path so that we don't have to do it again and again

        Spider.queuefile = Spider.projectname + '/queue.txt'
        Spider.crawledfile = Spider.projectname + '/crawled.txt'

        self.bootfile()

        # just to show user something is going on the spider is crawling the page
        self.crawlpage('First Spider', Spider.base_url)

    @staticmethod  # same for all spiders; we don't need to pass self as that is related to this particular class
    def bootfile():

        # first spider will create directory and  data files with the home page link only
        create_dir(Spider.projectname)
        create_data_files(Spider.projectname, Spider.base_url)
        Spider.queue = file_to_set(Spider.queuefile)  # get the text file and convert it to sets
        Spider.crawled = file_to_set(Spider.crawledfile)

    @staticmethod
    def crawlpage(spider_name, pageurl):
        # displaying what page are you crawling currently
        if pageurl not in Spider.crawled:
            print(spider_name + 'is now crawling' + pageurl)
            print('Queued files' + str(len(Spider.queue)) + '\n Crawled Files ' + str(len(Spider.crawled)))

            # collectlinks is to connect to webpage and return a set of all the links present on the webpage
            Spider.add_to_queue(Spider.collectlinks(pageurl))

            # update sets
            Spider.queue.remove(pageurl)
            Spider.crawled.add(pageurl)

            # update the actual files
            Spider.updatefiles()

    @staticmethod
    def collectlinks(pageurl):
        html_string = ''
        # to store the converted html string
        # to perform server or networking operations so as to avoid program crash
        # we use try: and except
        try:
            # to make the connection and store it's response
            connected = urlopen(pageurl)

            # inorder to check it is an html file
            if connected.getheader('Content-Type') == 'text/html':
                html_binary = connected.read()
                html_string = html_binary.decode('utf-8')
                # utf-8 is a type of character encoding

            # this html string is now in human readable format and can be passed on to findlinks file
            finder = LinkFinder(Spider.base_url, pageurl)
            finder.feed(html_string)
            # here it really parses it
        except:
            print('Error: Cannot find page')
            # we return an empty set for faulty url
            return set()
        return finder.page_links()

    @staticmethod
    def add_to_queue(urls):
        for url in urls:
            # check if it is already in queue or is crawled
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domainname not in url:
                continue
            # to crawl pages of that particular site only

            Spider.queue.add(url)

    @staticmethod
    def updatefiles():
        set_to_file(Spider.queue, Spider.queuefile)
        set_to_file(Spider.crawled, Spider.crawledfile)
