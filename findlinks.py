from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):  # we'll inherit from parser

    def __init__(self, base_url,
                 page_url):
        # dunder init; self represents the instance of the class which binds the attributes together
        super().__init__()  # using super classes init
        self.base_url = base_url  # to find the home page url
        self.page_url = page_url
        self.urls = set()  # all the crawled links will be stored here

    # HTML Parser reads only start tag because it has most of the urls and links
    # this function helps us add perfectly formatted url to the set
    def handle_start_tag(self, tag, attrs):
        # print(tag)                     to print tags that's it
        if tag == 'a':
            for (attribute, value) in attrs:
                # here attribute is the attributes in html in tags exp. href, class etc.
                if attribute == 'href':
                    link = parse.urljoin(self.base_url, value)  # for relative url
                    self.urls.add(link)

    def page_links(self):
        return self.urls

    def error(self, message):
        pass

# to read html tags that's it
# finder = LinkFinder() #we make HTML Parser an object
# finder.feed('<html><head><title> Vulnerability Scanner </Title></head>'
#           '<body><p> Parser </p></body></html>') #put in html from whatever page we are crawling
