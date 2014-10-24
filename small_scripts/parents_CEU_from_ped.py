#!/home/o_o/anaconda/bin/python


f1=open('integrated_call_samples.20130502.ALL.ped', 'r')
f2=open('ceu_to_subset', 'w')

f3 = f1.readlines()
f1.close()


for line in f3:
	line = line.split()
	if line[6] == 'CEU':
		if line[2]=='0' and line[3]=='0':
			f2.write("%s\n"%line[1])

f2.close()
