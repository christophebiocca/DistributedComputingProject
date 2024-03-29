import sys

if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 2):
    print("The Computing Collective regrets to inform you that your version of python is too low to be supported")
    exit()

import socket
import urllib.request
import subprocess
import sys
import urllib
import string
import os
import pickle
import http
import WorkUnit

serverUrl = "http://jknielse.twilightparadox.com/"
serverUrl = "http://localhost:1080/"

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

def getNewWorkUnit():
    data = urllib.parse.urlencode([("request", "newWorkUnit")]).encode("utf-8")
    response = urllib.request.urlopen(serverUrl, data).read()
    decodedData = urllib.parse.unquote_to_bytes(response)
    unpickledWorkUnit = pickle.loads(decodedData)
    return unpickledWorkUnit

def sendResults(values):
    data = urllib.parse.urlencode([("request", "reportValues"), ("matchingValues", urllib.parse.quote_from_bytes(pickle.dumps(values)))]).encode("utf-8")
    response = urllib.request.urlopen(serverUrl, data)

while True:
    try:
        if os.path.isfile(customerFile):
            workUnit = getNewWorkUnit()

            start = workUnit.rangeStart
            end = workUnit.rangeEnd

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
    except(urllib.error.URLError,socket.error,http.client.BadStatusLine):
        pass
