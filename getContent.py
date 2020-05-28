# gets the file content from the file URLS
import requests
import base64

# returns the fileSize of the desired file given the url
def getFileContents(fileURL, authCreds):
    
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
    
    # get file bytes and decode them
    resultData = resp.json()
    fileEncoding = resultData['encoding'].rstrip('\n')
    
    if (fileEncoding != 'base64'):
         print(f'file encoding is {fileEncoding}')
     
    fileBytesEncoded = resultData['content']
    fileBytesDecoded = base64.b64decode(fileBytesEncoded)
    fileASCII = fileBytesDecoded.decode('utf-8')

    return fileASCII

contentURLFile = open('Data/desiredFiles.txt', 'r')
contentURLs = contentURLFile.readlines()
contentURLFile.close()

authFile = open('authInfo.txt', 'r')
username = authFile.readline().rstrip('\n')
secret = authFile.readline().rstrip('\n')
authFile.close()

# gets contents of all desired files and saves them
for i in range(len(contentURLs)):
     
     # make a request for file contents to the Github API
     currContentURL = contentURLs[i].rstrip('\n')
     fileContents = getFileContents(currContentURL, (username, secret))

     fileName = 'file' + str(i) + '.py'

     # open file with fileName and output content into it
     filePy = open(f'Data/Desired_Files/{fileName}', 'w')
     filePy.write(fileContents)
     filePy.close()

print('DONE!')
