#!/home/laba/anaconda/bin/python

f1=open('relationships_w_pops_041510.txt', 'r')

f2=f1.readlines()
independent=open('independent', 'w')

f1.close()

for line in f2:
	line=line.split()
	if line[6]=='CEU':
		if line[2]=='0' and line[3]=='0':
			independent.write("%s\n"%'\t'.join(line))


independent.close()
