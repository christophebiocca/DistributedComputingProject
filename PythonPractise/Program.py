import urllib.request
import subprocess
import sys
import urllib

returnedLines = subprocess.Popen("TestProgram.exe 10 100", stdout=subprocess.PIPE)

while True:
    line = returnedLines.stdout.readline() 
    if line:
        print(int(line))
    else:
        break