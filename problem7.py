from common import prime

N = 6
def find_prime(num):
    p = 0
    n = 1
    while(p < 10001):
        while True:
            n += 1
            if(prime(n)):
                break
        p += 1
    return n;

print find_prime(N)
