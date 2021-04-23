# Run a .rusted file
import sys 
import rustedscript

def checkForComments(line):
	indexOfComment = int( line.find("//") )
	if indexOfComment == -1:
		indexOfComment = int( line.find("#") )
	if indexOfComment == -1:
		indexOfComment = int( line.find("/*") )
	if indexOfComment != -1:
		newline=line[0:indexOfComment-1]
	else:
		newline=line
	return newline

with open(sys.argv[1]) as rustedfile: # open the rusted file
	print("    Running {}".format(sys.argv[1])+'...\n')
	lines = rustedfile.readlines()
	cnt=0
	for line in lines:
		if len(checkForComments(line))>0:
			if int(line.find('use("')) != -1:
				start=int(line.find('("'))
				end=int(line.find('")'))
				# try:
				fileToInclude=open(line[start+2:end],'r')
				# except FileNotFoundError:
				# 	print("FATAL: File {} not found.".format(line[start+2:end]))
				# 	sys.exit(1)
				linesOfFileToInclude = fileToInclude.readlines()
				for line in linesOfFileToInclude:
					if len(line)==1:
						remove=0
					else:
						remove=1
					rustedscript.run('<stdin>', checkForComments(line)[0:len(line)-remove])
			if len(checkForComments(line))==1:
				remove=0
			else:
				remove=1
			result, error = rustedscript.run('<stdin>', checkForComments(line)[0:len(line)-remove])
			if error:
				print(error.as_string())
				print("\n---- \n FATAL: Process exited with non-zero exit code")
				sys.exit(1)
			elif result:
				print(result)
			cnt+=1
	print("\n---- \n SUCCESS: {} ran successfully".format(sys.argv[1]))



