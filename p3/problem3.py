N = 600851475143

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def prime(num):
    if len(factors(num)) > 2:
        return False
    return True

print sorted(filter(prime, factors(N))) [-1]
