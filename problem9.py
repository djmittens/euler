from common import *

print filter(lambda x: len(x) > 0 and x[0] > 0, [map(lambda x: x[0] * x[1] * x[2], filter( lambda x: x[0] + x[1] + x[2] == 1000, map(lambda x: [x[0]**2 - x[1]**2, 2 * x[0] * x[1], x[0]**2 + x[1]**2], map(lambda x: [x, i / x], factors(i))))) for i in xrange(2, 1000, 2)])
