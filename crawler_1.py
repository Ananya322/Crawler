import os


# each website you crawl is a separate project with a separate folder
def create_dir(directory):
    if not os.path.exists(directory):
        print("Creating Project" + directory)
        os.makedirs(directory)


# create_dir('Vulnerability Scanner')


# creating new file
def create_new_file(path, data):
    a = open(path, 'w')
    a.write(data)
    # write mode to add data to it
    a.close()
    # frees memory resources to prevent data leak


# create queue and crawled files
def create_data_files(projectname, baseurl):
    queue = projectname + '/queue.txt'
    # queue.txt is the file present in Vulnerability Scanner which will contain the list of urls_set to be scanned
    crawled = projectname + '/crawled.txt'
    # crawled.txt will contain files that are already crawled
    if not os.path.isfile(queue):
        create_new_file(queue, baseurl)  # if any file is not crawled in the list and no dir is present
    if not os.path.isfile(crawled):
        create_new_file(crawled, '')


# create_data_files('Vulnerability Scanner', '
# https://towardsdatascience.com/how-to-build-a-simple-web-crawler-66082fc82470?gi=5fa3e612c6de')

# adding data(link) into existing file
def append(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# delete data from the file
def delete_content(path):
    with open(path, 'w'):
        # w == write mode
        pass
        # do nothing


# with sets there will be no cross overs
# read a file and convert it to set
def file_to_set(filename):
    results = set()
    with open(filename, 'rt') as a:  # rt == read text file ; loop thru the file line by line
        for line in a:
            results.add(line.replace('\n', ''))
            # while making file we added new line character we don't want that in set so we replace it with nothing using builtin function .replace('','')
    return results


# convert set to a file
def set_to_file(urls_set, file):
    delete_content(file)
    # looping thru the set
    for urls_set in sorted(urls_set):
        append(file, urls_set)  # append data to files
