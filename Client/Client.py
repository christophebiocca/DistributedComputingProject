#!/usr/local/bin/python3.2
import urllib.request
import subprocess
import sys
import urllib
import string

serverUrl = "http://jknielse.twilightparadox.com:80/"

while True:
    range = list(map(int, urllib.request.urlopen(serverUrl).read().split()))

    start = range[0]
    end = range[1]

    usercode = subprocess.Popen("TestProgram.exe " + str(start) + " " + str(end), stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    while True:
        line = usercode.stdout.readline() 
        if line:
            data = urllib.parse.urlencode([("newCustCode", False), ("matchedValue", int(line))]).encode("utf-8")
            postResponse = urllib.request.urlopen(serverUrl, data).read()
        else:
            break
