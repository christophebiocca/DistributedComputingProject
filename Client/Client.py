import urllib.request
import subprocess
import sys
import urllib

start = int(sys.stdin.readline())
end = int(sys.stdin.readline())

usercode = subprocess.Popen("TestProgram.exe " + str(start) + " " + str(end), stdout=subprocess.PIPE)
while True:
    line = usercode.stdout.readline() 
    if line:
        print(int(line))
    else:
        break