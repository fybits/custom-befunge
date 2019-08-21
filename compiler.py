#!/usr/bin/python3

from os import chmod

codeSize = 128

def make_standalone(filename: str):
	code = [ list(" "*codeSize) for x in range(codeSize) ]
	handle = open(filename,"r")
	lines = [ x.replace("\n","") for x in handle.readlines() ]
	handle.close()
	for i in range(min(len(lines),codeSize)):
		for j in range(min(len(lines[i]),codeSize)):
			code[j][i] = lines[i][j]
	
	outFilename = ""
	if '.' in filename:
		outFilename = filename.split('.')[0]+".py"
	else:
		outFilename = filename+".py"

	out = open(outFilename, "w")
	coreFile = open("core.py", "r")

	out.writelines(coreFile.readlines())
	coreFile.close()

	out.write("\n\ncode = "+str(code))
	out.write("\nrun(code)\n")
	out.close()
	chmod(outFilename,0o777)

make_standalone("test.fu")