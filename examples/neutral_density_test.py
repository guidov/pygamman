import numpy as np
from pygamman import gamman as nds

#Test simple part of gn
atg=nds.atg(35.0,10.0,1000)
print atg

#test the module by replicating example.f
# create a data set the same as example.dat

alon,alat,n=np.array([187.317,-41.6667,24])
stp= np.array([  
  [35.0660,  12.2500,     1.0],\
  [35.0860,  12.2100,    48.0],\
  [35.0890,  12.0900,    97.0],\
  [35.0780,  11.9900,   145.0],\
  [35.0250,  11.6900,   194.0],\
  [34.8510,  10.5400,   291.0],\
  [34.6960,   9.3500,   388.0],\
  [34.5720,   8.3600,   485.0],\
  [34.5310,   7.8600,   581.0],\
  [34.5090,   7.4300,   678.0],\
  [34.4960,   6.8700,   775.0],\
  [34.4520,   6.0400,   872.0],\
  [34.4580,   5.5000,   969.0],\
  [34.4560,   4.9000,  1066.0],\
  [34.4880,   4.0400,  1260.0],\
  [34.5360,   3.2900,  1454.0],\
  [34.5790,   2.7800,  1647.0],\
  [34.6120,   2.4500,  1841.0],\
  [34.6420,   2.2110,  2020.0],\
  [34.6570,   2.0110,  2216.0],\
  [34.6850,   1.8940,  2413.0],\
  [34.7070,   1.7880,  2611.0],\
  [34.7200,   1.5540,  2878.0],\
  [34.7290,   1.3800,  3000.0]])

s=np.array(stp[:,0])
t=np.array(stp[:,1])
p=np.array(stp[:,2])

print n
print s
print t
print p
print alon
print alat
print len(s)


#test pygamman (calculate gamma_n at p)
gamma_n,dgl,dgh = nds.gamma_n(s,t,p,24,alon,alat)

print "Printing gamma_n:"
print gamma_n,dgl,dgh
print dgl
print dgh
# test neutral_density surfaces (i.e. calculate s,t,p at neutral density levels: glevels)
nz=80 # not used
nlevels=3
glevels=np.array([26.8,27.9,28.1])

sns,tns,pns,dsns,dtns,dpns = nds.neutral_surfaces(s,t,p,gamma_n,n,glevels,nlevels)

print "Printing neutral_surfaces:"
print glevels
print sns
print tns
print pns
print dpns


