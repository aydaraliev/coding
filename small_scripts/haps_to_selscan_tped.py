#!/home/o_o/anaconda/bin/python

import sys


f1le = open(sys.argv[1], 'r')
f3le = open(sys.argv[2]+'.tped', 'w')

f2le = f1le.readlines()

f1le.close()

for line in f2le:
	line = line.split()
	line[3]=line[2]
	del line[4]
	f3le.write('%s\n'%'\t'.join(line))

f3le.close()
	
