#!/home/o_o/anaconda/bin/python

ceu=open('ceu_samples', 'w')
pops=open('relationships_w_pops_041510.txt','r')

f1=pops.readlines()
pops.close()

for line in f1:
	line=line.split()
	if line[6]=='CEU':
		ceu.write('%s\n'%'\t'.join(line))
ceu.close()

"""with open('relationships_w_pops_041510.txt', 'r') as f1:
	data=f1.readlines()
	for l in data:
		z=l.split()
		if z[6]=='CEU':
			ceu.write('%s\n'%'\t'.join(z))"""
