# Github API requester
import queue
import requests
from ratelimit import limits, RateLimitException
from backoff import on_exception, expo
import time
import pprint

ONE_MINUTE = 60
TIME_ALOTTED = time.perf_counter() + 60

def backoff_hdlr(details):
    
    # using the global variable LAST_TIME
    global TIME_ALOTTED

    # wait the minimum time necessary before we can make another request
    currTime = time.perf_counter()
    waitTime = TIME_ALOTTED - currTime
    print("SLEEPS")
    print(waitTime)
    time.sleep(waitTime)

    # update the time alotted for another 30 requests to be made
    TIME_ALOTTED = time.perf_counter() + 60

    return None
    

# this decoration will not allow this function to make more than 30 API calls per minute
# if rate is exceeded then will wait 60 seconds to make another request and then use an exponential back off method
@on_exception(expo, RateLimitException, on_backoff=backoff_hdlr, max_tries=8)
@limits(calls=30, period=ONE_MINUTE)
def callGitAPI(repoName, authCreds):
    
    # prep github API call to look for python files that include BeautifulSoup
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


# making requests to github for each repoName
TIME_ALOTTED = time.perf_counter() + 60

for i in range(60):

    # update TIME_ALOTTED every 60 seconds if there are less than 30 reqs happening per min
    currTime = time.perf_counter()
    if (currTime > TIME_ALOTTED):
        TIME_ALOTTED = time.perf_counter() + 60
    
    # make a req for the new repoName
    currRepo = repoQueue.get()
    resp = callGitAPI(currRepo, (username, token))

    # if there are any results record them
    if resp['total_count'] > 0:
        for it in resp['items']:
            it['repository']
        pp = pprint.PrettyPrinter(indent=3)
        pp.pprint(resp)
