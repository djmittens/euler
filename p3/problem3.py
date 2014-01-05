from multiprocessing import Pool

def prime(num):
    if num == 1:
        return False
    if num % 2 == 0:
        return False
    for i in xrange(3, num / 2, 1) :
        if num % i == 0:
            return False
    return True
pool = Pool(4)
N = 600851475143

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
print factors(N)
