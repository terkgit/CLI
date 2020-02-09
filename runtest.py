import os
import subprocess
import sys
import time


print("before")
testFile=open("test.out","w+")
subprocess.Popen("testapp.bat",stdout=testFile)
# pid = subprocess.Popen([sys.executable, "testapp.bat"])
# os.system("start testapp.bat -> test.out")
count=0
outFile=open("test.out","r")

for i in range(20):
	count=0
	for line in outFile:
		print(line, end = '')
		count+=1
	# print("__",count)
	time.sleep(1)
print("after")
