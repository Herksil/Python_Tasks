import sys
from random import uniform
n=int(sys.argv[1],10)
i=0
sum=0.0
while i<n:
    a=uniform(-1,1)
    sum=sum+a
    print ("%.4f" % (a))
    i=i+1
middle=sum/n
print("middle = ","%.4f" % (middle))