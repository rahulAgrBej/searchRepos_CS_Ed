# Github API requester
import queue
import requests
from ratelimit import limits

ONE_MINUTE = 60

# this decoration will not allow this function to make more than 30 API calls per minute
@limits(calls=30, period=ONE_MINUTE)
def callGitAPI(repoName, auth):
    # prep github API call
    return None

# read file for authentication information
authFile = open('authInfo.txt', 'r')
username = authFile.readline().rstrip('\n')
token = authFile.readline().rstrip('\n')
authFile.close()

print(username)
print(token)

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

