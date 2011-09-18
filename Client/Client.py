import urllib.request
import subprocess
import sys
import urllib
import string
import os

serverUrl = "http://129.97.224.134/"
serverUrl = "http://localhost:1080/"
customerFile = "TestProgram.exe"

def getNewProgram():
    file = open(customerFile, "wb")
    data = urllib.parse.urlencode([("request", "newProgram")]).encode("utf-8")
    response = urllib.request.urlopen(serverUrl, data).read()
    file.write(response)
    file.close()

def getNewRange():
    data = urllib.parse.urlencode([("request", "newRange")]).encode("utf-8")
    response = urllib.request.urlopen(serverUrl, data).read()
    return list(map(int, response.split()))

while True:
    if os.path.isfile(customerFile):
        range = getNewRange()

        start = range[0]
        end = range[1]

        usercode = subprocess.Popen(customerFile + " " + str(start) + " " + str(end), stdout=subprocess.PIPE, stdin=subprocess.PIPE)

        while True:
            line = usercode.stdout.readline() 
            if line:
                data = urllib.parse.urlencode([("request", "reportValue"), ("matchedValue", int(line))]).encode("utf-8")
                postResponse = urllib.request.urlopen(serverUrl, data)
            else:
                break
    else:
        getNewProgram()