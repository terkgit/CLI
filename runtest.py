import os
import subprocess
import time


testFile=open("test.out","w+")
subprocess.Popen("testapp.bat",stdout=testFile)
outFile=open("test.out","r")
idleCount=0
keepRunning=True
while (keepRunning):
	count=0
	for line in outFile:
		print(line, end = '')
		count+=1
		if ("Test Passed" in line):
			keepRunning=False
	if (count==0):
		idleCount+=1
	else:
		idleCount=0
	if (idleCount>=6):
		keepRunning=False
	# print("__",count)
	time.sleep(1)
print("after")
