# Github API requester
import queue
import requests
import time
from datetime import datetime
import math

ONE_MINUTE = 60

def searchGitAPI(repoName, authCreds):
    
    # prep github API call to look for python files that include BeautifulSoup
    gitAPIQuery = 'https://api.github.com/search/code?q=BeautifulSoup+in:file+language:python+repo:'
    fullQuery = gitAPIQuery + repoName
    response = requests.get(fullQuery, auth=authCreds)
    if response.status_code != 200:
        print(response)
        print(response.content)

    # check the request header to see if there are any remaining requests for this window
    reqsRemaining = int(response.headers['X-RateLimit-Remaining'])
    waitTime = 0
    
    # check to see when X-RateLimit-Reset happens to resume requests (in UTC epoch seconds)
    if (reqsRemaining == 0):
        reqReset = datetime.fromtimestamp(int(response.headers['X-RateLimit-Reset']))
        currTime = datetime.now()
        waitTime = math.ceil((reqReset - currTime).total_seconds())
        if waitTime == 0:
            waitTime = 1

    if response.status_code != 200:
        return {'total_count': 0}, waitTime

    return response.json(), waitTime

# read file for authentication information
authFile = open('authInfo.txt', 'r')
username = authFile.readline().rstrip('\n')
token = authFile.readline().rstrip('\n')
authFile.close()

# repoName queue
repoQueue = queue.Queue()

# read through git repo name list and put into a queue
repoFile = open('Data/reposORDERED.txt', 'r')

# get total repo count
repoTotal = int(repoFile.readline())

for idx in range(repoTotal):
    
    # remove any trailing newlines and add to queue
    repoName = (repoFile.readline()).rstrip('\n')
    repoQueue.put(repoName)

repoFile.close()

# opening file to write all the URL of the desired files
desiredFiles = open('Data/desiredFiles.txt', 'w')

# making requests to github for each repoName

for i in range(repoTotal):

    # make a req for the new repoName
    currRepo = repoQueue.get()
    resp, waitTime = searchGitAPI(currRepo, (username, token))

    # if there are any results record them
    if resp['total_count'] > 0:
        for it in resp['items']:
            
            # form correct get contents URL request
            filePath = it['path']
            repoFullName = it['repository']['full_name']
            gitFileContentsURL = "https://api.github.com/repos/" + repoFullName + '/contents/' + filePath
            desiredFiles.write(gitFileContentsURL)
            desiredFiles.write('\n')
    
    if waitTime > 0:
        time.sleep(waitTime)

    if i % 100 == 0:
        print(f'Requested {i} so far')

desiredFiles.close()