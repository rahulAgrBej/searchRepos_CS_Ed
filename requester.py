# Github API requester
import queue
import requests
from ratelimit import limits, RateLimitException
from backoff import on_exception, expo
import time
import pprint

ONE_MINUTE = 60

def backoff_hdlr(details):
    print("SLEEPS")
    time.sleep(60)
    

# this decoration will not allow this function to make more than 30 API calls per minute
# if rate is exceeded then will wait 60 seconds to make another request and then use an exponential back off method
@on_exception(expo, RateLimitException, on_backoff=backoff_hdlr, max_tries=8)
@limits(calls=30, period=ONE_MINUTE)
def callGitAPI(repoName, authCreds):#####, lastTime):
    # prep github API call
    '''
    currTime = time.perf_counter()
    diffTime = currTime - lastTime
    if (diffTime < 2):
        time.sleep(2-diffTime)
    '''
    gitAPIQuery = 'https://api.github.com/search/code?q=BeautifulSoup+in:file+language:python+repo:'
    fullQuery = gitAPIQuery + repoName
    response = requests.get(fullQuery, auth=authCreds)
    #########lastTime = time.perf_counter()

    if response.status_code != 200:
        return {'total_count': 0}####, lastTime

    return response.json()#####, lastTime

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

#####lastTime = time.perf_counter()
for i in range(30):
    currRepo = repoQueue.get()
    resp = callGitAPI(currRepo, (username, token))####, lastTime)
    if resp['total_count'] > 0:
        pp = pprint.PrettyPrinter(indent=3)
        pp.pprint(resp)
