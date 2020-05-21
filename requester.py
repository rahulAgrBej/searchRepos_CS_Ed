# Github API requester
import queue
import requests
from ratelimit import limits, RateLimitException
from backoff import on_exception, expo
import time

ONE_MINUTE = 60

def backoff_hdlr(details):
    print("SLEEPS")
    time.sleep(30)
    

# this decoration will not allow this function to make more than 30 API calls per minute
# if rate is exceeded us an exponential back off method to better time requests
@on_exception(expo, RateLimitException, on_backoff=backoff_hdlr, max_tries=8)
@limits(calls=30, period=ONE_MINUTE)
def callGitAPI(repoName, authCreds):
    # prep github API call

    gitAPIQuery = 'https://api.github.com/search/code?q=BeautifulSoup+in:file+language:python+repo:'
    fullQuery = gitAPIQuery + repoName
    response = requests.get(fullQuery, auth=authCreds)

    if response.status_code != 200:
        return {'total_count': 0}
    return response.json()

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

# testing authentication token

for i in range(30):
    currRepo = repoQueue.get()
    resp = callGitAPI(currRepo, (username, token))
    if resp['total_count'] > 0:
        print('FOUND ONE!!!!')
        for it in resp['items']:
            print(currRepo)
            print(it['name'])
    else:
        print("NOPE")

print("DONE")
