from common import factors
from common import prime

N = 20
def check(num):
    print num
    print filter(lambda x: num % x != 0, range(1, N+1))

print filter(prime, range(1,20))
check (reduce(lambda x, y: x * y, filter(prime, range(3, N))) * 3 * 16)

