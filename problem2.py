from array import *

N = 4000000

d = array('i', [1,1])
c = 1

while (c < N):
    d.append(c)
    c = d[-1] + d[-2]

print d
print sum(filter(lambda x: x % 2 == 0, d) )
