import subprocess

def numDevices(cmd):
	cmd = [cmd]
	subprocess.call(cmd, shell=True)
	numDevices = open('numDevices.txt').readlines()
	num = numDevices[0].split()[-2]

	return num


if __name__ == "__main__":
	numDevices("./RUN.sh")