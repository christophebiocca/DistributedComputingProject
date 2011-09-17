import urllib.request
import subprocess
import sys
import urllib



clientInterface = subprocess.Popen(r"C:\Python32\python.exe ..\Client\Client.py", stdin=subprocess.PIPE, stdout=subprocess.PIPE)

sys.stdout.writelines("lol")

while True:
    line = clientInterface.stdout.readline()
    if line:
        print(int(line))
    else:
        break
