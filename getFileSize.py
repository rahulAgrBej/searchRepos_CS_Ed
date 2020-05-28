import requests

# returns the fileSize of the desired file given the url
def getSize(fileURL, authCreds):
    
    resp = requests.get(fileURL, auth=authCreds)
    
    print(resp.status_code)
    
    while resp.status_code == 403:
        time.sleep(60)
        print('retrying previous 403 request')
        resp = requests.get(fileURL, auth=authCreds)

    # check the request header to see if there are any remaining requests for this window
    reqsRemaining = int(resp.headers['X-RateLimit-Remaining'])
    waitTime = 0
    
    # check to see when X-RateLimit-Reset happens to resume requests (in UTC epoch seconds)
    if (reqsRemaining == 0):
        reqReset = datetime.fromtimestamp(int(resp.headers['X-RateLimit-Reset']))
        currTime = datetime.now()
        waitTime = math.ceil((reqReset - currTime).total_seconds())
    
    # get file size
    resultData = resp.json()
    fileSize = resultData['size']

    return fileSize

# Get all desired file urls
urlFile = open('Data/desiredFiles.txt', 'r')
urls = urlFile.readlines()
urlFile.close()

# Get authentication information
authFile = open('authInfo.txt', 'r')
username = authFile.readline().rstrip('\n')
secret = authFile.readline().rstrip('\n')
authFile.close()

sizeSum = 0

for i in range(len(urls)):

    currURL = urls[i].rstrip('\n')
    sizeSum += getSize(currURL, (username, secret))

print(f'total file size: {sumSize}')