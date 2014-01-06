from common import *

for i in xrange(2, 1000, 2):
    r = filter( lambda x: x[0] + x[1] + x[2] == 1000, map(lambda x: [x[0]**2 - x[1]**2, 2 * x[0] * x[1], x[0]**2 + x[1]**2], map(lambda x: [x, i / x], factors(i))))
    if len(r) > 0:
        print r
        print map(lambda x: x[0] * x[1] * x[2], r)
