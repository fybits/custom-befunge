#!/usr/bin/python3

from sys import argv
import core

def run_file(filename):
	code = [ list(" "*core.codeSize) for x in range(core.codeSize) ]
	handle = open(filename,"r")
	lines = [ x.replace("\n","") for x in handle.readlines() ]
	handle.close()
	for i in range(min(len(lines),core.codeSize)):
		for j in range(min(len(lines[i]),core.codeSize)):
			code[j][i] = lines[i][j]
	
	core.run(code)

run_file("test.fu")

if len(argv) > 1:
	run_file(argv[1])
else:
	print("Usage:")
	print("\t"+argv[0]+" (filename)")