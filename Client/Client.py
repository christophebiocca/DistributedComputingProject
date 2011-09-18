import sys

if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 2):
    print("The Computing Collective regrets to inform you that your version of python is too low to be supported")
    exit()

import urllib.request
import subprocess
import sys
import urllib
import string
import os
import pickle

serverUrl = "http://jknielse.twilightparadox.com/"
#serverUrl = "http://localhost:1080/"

if os.name == "posix":
    customerFile = "CrossPlatformTestProgram.linux"
elif os.name == "nt":
    customerFile = "CrossPlatformTestProgram.exe"
elif os.name == "mac":
    customerFile = "CrossPlatformTestProgram.mac"

def downloadNewProgram():
    file = open(customerFile, "wb")
    data = urllib.parse.urlencode([("request", "newProgram"),("platform",urllib.parse.quote_from_bytes(pickle.dumps(os.name)))]).encode("utf-8")
    response = urllib.request.urlopen(serverUrl, data).read()
    file.write(response)
    file.close()
    if os.name == "posix":
        os.chmod(customerFile, 777)

def getNewRange():
    data = urllib.parse.urlencode([("request", "newRange")]).encode("utf-8")
    response = urllib.request.urlopen(serverUrl, data).read()
    return list(map(int, response.split()))

def sendResults(values):
    data = urllib.parse.urlencode([("request", "reportValues"), ("matchingValues", urllib.parse.quote_from_bytes(pickle.dumps(values)))]).encode("utf-8")
    response = urllib.request.urlopen(serverUrl, data)

while True:
    if os.path.isfile(customerFile):
        range = getNewRange()

        start = range[0]
        end = range[1]

        if os.name == "posix" or os.name == "mac":
            usercode = subprocess.Popen(["./" + customerFile, str(start), str(end)], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        elif os.name == "nt": 
            usercode = subprocess.Popen(customerFile + " " + str(start) + " " + str(end), stdout=subprocess.PIPE, stdin=subprocess.PIPE)

        data = []
        while True:
            line = usercode.stdout.readline() 
            if not line:
                break
            data.append(int(line))

        sendResults(data)
    else:
        downloadNewProgram()
