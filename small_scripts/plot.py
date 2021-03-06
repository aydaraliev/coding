#!/home/laba/anaconda/bin/python
import sys
import matplotlib.pyplot as plt


print sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
f=open(sys.argv[1])
f2=open(sys.argv[2])
f3=open(sys.argv[3])
f4=open(sys.argv[4])

pop2=f.readlines()
pop3=f2.readlines()
pop4=f3.readlines()
pop5=f4.readlines()
f.close()
f2.close()
f3.close()
f4.close()

iHS2=[]
iHS3=[]
iHS4=[]
iHS5=[]
pos2=[]
pos3=[]
pos4=[]
pos5=[]

"""iHS=[]
test=f1[0].strip()
test
print test[2], test[5]
print Decimal(test[2]), Decimal(test[5])"""

for line in pop2:
	row = line.split()
	e=abs(float(row[5]))
	p=int(row[1])
	if e > 2.5:
		iHS2.append(e)
		pos2.append(p)

for line in pop3:
	row = line.split()
	e=abs(float(row[5]))
	p=int(row[1])
	if e > 2.5:
		iHS3.append(e)
		pos3.append(p)

for line in pop4:
	row = line.split()
	e=abs(float(row[5]))
	p=int(row[1])
	if e > 1.5:
		iHS4.append(e)
		pos4.append(p)

for line in pop5:
	row = line.split()
	e=abs(float(row[5]))
	p=int(row[1])
	if e > 1.5:
		iHS5.append(e)
		pos5.append(p)
	
plt.figure(1)
#plot Ijma
plt.subplot(4,1,1)
plt.scatter(pos2, iHS2, s=[10], c='b')
plt.ylim(2.4, 5)
plt.title('Ijma')
#plt.xlim(-0.01*10**8, 2.5*10**8 )
#plot Obiachevo
plt.subplot(4,1,2)
plt.scatter(pos3, iHS3, s=[10], c='g')
plt.ylim(2.4,5)
plt.title('Obiachevo')
#plt.show()
#plot CEU
plt.subplot(4,1,3)
plt.scatter(pos4, iHS4, s=[10], c='r')
plt.ylim(1.3, 3)
plt.title('CEU')
plt.subplot(4,1,4)
plt.scatter(pos5, iHS5, s=[10], c='g')
plt.ylim(1.4, 5)
plt.title('CEU_hapmap')
#Save figure
plt.savefig(sys.argv[5], format='png')
