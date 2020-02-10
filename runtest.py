import subprocess
import time
import sys

executeFile="testapp.bat"
outputFileName="test.out"
doneText="Test Passed"

def main():
	# execute testapp.bat > test.out 
	outputFile=open(outputFileName,"w+")
	p=subprocess.Popen(executeFile, stdout=outputFile, shell=False)
	print(p.pid)
	
	result=waitForTest(p,6) # side effect, print test output periodicly
	if result=="TimeoutExpired":
		p.kill()
		p.communicate()
		outputFile.write("Test Timeout, termination test execution ...\n")
		outputFile.close()

	# old implementation 
	# print test output so far and check if test is finished
	# result=isRunning()
	# if result=="timeout":
	# 	outputFile.write("Test Timeout, termination test execution ...\n")
	# 	sys.exit("Test Timeout")

# wait for test to finish or timeout after ~timeoutCount seconds
# side efect - prints updated outFile 
def waitForTest(p,timeoutCount):
	outFile=open(outputFileName,"r")
	while timeoutCount>0:
		for line in outFile:
			print(line, end = '')
			if doneText in line:
				return "Done"
		try:
			res=p.wait(1)
			return "Done"
		except subprocess.TimeoutExpired: 
			pass
		timeoutCount-=1
	return "TimeoutExpired"
			

# old implementation
# def isRunning():
# 	outFile=open("test.out","r")
# 	idleCount=0 		# timeout after idleCount reaches 6
# 	keepRunning=True	# keep running flag
# 	while keepRunning:
# 		count=0
# 		for line in outFile:
# 			print(line, end = '')
# 			count+=1
# 			if "Test Passed" in line:
# 				keepRunning=False
# 		if count==0:	# no new lines were printed (test is idle)
# 			idleCount+=1
# 		else:
# 			idleCount=0
# 		if idleCount>=6:	# idle timeout
# 			keepRunning=False
# 		time.sleep(1)
# 	return "timeout"

# execution of main 
if __name__=="__main__":
   main()

