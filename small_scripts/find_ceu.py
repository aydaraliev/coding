#!/home/laba/anaconda/bin/python

f=open('/home/laba/Desktop/CEU/ceu.txt')
f1=open('/media/laba/224846924846649F/1k/Omni25_genotypes_2141_samples.b36.v2.vcf')
ceu_in_vcf=open('/home/laba/Desktop/CEU/ceu_to_subset.txt', 'w')


ceu = []
vcf_line=[]
final_inds=[]

with f as ind_list:
	for ind in ind_list:
		ceu.append(ind.strip())

with f1 as l:
	for line in l:
		if line.split()[0]=='#CHROM':
			vcf_line=line.split()
			break
for ind in ceu:
	if ind in vcf_line:
		final_inds.append(ind)


"""for ind in ceu:
	for ind2 in vcf_line:
		if ind==ind2:	
			final_inds.append(ind)"""

print len(final_inds)

for ind in final_inds:
	ceu_in_vcf.write('%s\n'%ind)


ceu_in_vcf.close()

