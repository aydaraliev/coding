#!/home/laba/anaconda/bin/python

f=open('ki_phased_tped.tped')
conv=open('ki_phased_converted.tped', 'w')
f2=f.readlines()
for line in f2:
    kilst=line.split()
    a=0
    z=0
    for c,x in enumerate(kilst):
        if kilst[c].isupper():
            z=c
            a=kilst[c]
            break
    for c,x in enumerate(kilst):
        if kilst[c]==a:
            kilst[c]='1'
    for c,x in enumerate(kilst):
        if kilst[c].isupper():
            kilst[c]='0'
    kilst[2]=kilst[3]
    to_write='\t'.join(kilst)
    conv.write('%s\n'%to_write)
f.close()
conv.close()
