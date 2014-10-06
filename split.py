#!/home/laba/anaconda/bin/python

from collections import Counter

f1le=open('ki_phased_conv_pop2.tped', 'r')
f=f1le.readlines()
chr=[]
dict=Counter()
for line in f:
	l1st=line.split()
	chr.append(l1st[0])
for elem in chr:
	dict[elem]+=1
print dict.keys()
chromosomes = dict.keys()
chromosomes.sort()
for i in chromosomes:
	sep_chr = open(i+'.tped', 'w')
	for x in f:
		if x[0]==i:
			sep_chr.write(x)
	sep_chr.close()
