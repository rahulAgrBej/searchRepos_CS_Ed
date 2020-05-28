# gets the file content from the file URLS
import requests
import base64

contentURLFile = open('Data/desiredFiles.txt', 'r')
contentURLs = contentURLFile.readlines()
contentURLFile.close()

authFile = open('authInfo.txt', 'r')
username = authFile.readline()
secret = authFile.readline()
authFile.close()


# gets contents of all desired files and saves them
for i in range(len(contentURLs)):
     
     currContentURL = contentURLs[i].rstrip('\n')
     print(currContentURL)

     resp = requests.get(currContentURL, auth=(username, secret))
     print(resp.headers)
     resultData = resp.json()
     print(f'response code: {resp.status_code}')
     print(resultData.keys())
     print(resultData['name'])
     print(f'file size: {resultData["size"]}')

     fileName = resultData['name']
     fileBytesEncoded = resultData['content']
     fileBytesDecoded = base64.b64decode(fileBytesEncoded)
     fileASCII = fileBytesDecoded.decode('ascii')

     # open file with fileName and output content into it
     filePy = open(f'Data/Desired_Files/{fileName}', 'w')
     filePy.write(fileASCII)
     filePy.close()

     break
