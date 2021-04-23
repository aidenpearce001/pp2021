import subprocess
import sys 
import os

inner_cmd = [,"cat","rff","wtf"]
def ls(file_type):
	import glob 

	for i in glob.glob("*"+file_type):
		print(i)

def cat(file):
	with open(file,'r') as c:
		for i in c:
			print(i)

def rff(filename):
	# This funtion excute command from file

	with open(filename,'r+') as f:
		for _ in f:
			subpocess.run(_.rstrip().split(" "))


def wtf(filename, cmd):
	# This funtion output the result of command to file

	f = open(filename, "w")
	subprocess.call(cmd.split(" "), stdout=f)


def help():
	print("""
		Some Inner command that you can use
		cat <file> (Read all content in file) 
		rff <file> (Excute all commend from file line by line)
		wtf <linux command> <file> (Write command result to file)
		""")

while True:
	try:
		cmd = input("[ >>> ] :")

		# subpocess.run(command)

		command = cmd.split(" ")
		if command[0] in inner_cmd:
			locals()[command[0]](command[1:])
		else:
			subpocess.run(command)

	except KeyboardInterrupt:
		print('Interrupted')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
	except Exception as E:
		print("Command not valid")
		help()
