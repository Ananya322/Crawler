#functions for extracting domain names only

from urllib.parse import urlparse

# function to get subdomain name from long url (abc.abc.vunerabilityscanner.com)
def get_subdomainname(url):
    try:
        #give url and the function will parse thru it and return the network location
        return urlparse(url).netloc

    except:
        return ''

#get domainname(vunerabilityscanner.com)
def get_domainname(url):
    try:
        result = get_subdomainname(url).split('.')
        return result[-2] + '.' + result[-1]

    except:
        return '' 



