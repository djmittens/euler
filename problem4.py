from common import factors

N = 999 * 999

def palindrome(num):
    num = str(num)
    n = len(num) // 2

    if num[0:n][::-1] == num[n if n % 2 != 0 else n + 1 : ]:
        return True
    else:
        return False

#Check to see  if there is a factor of length 3 that matches with another length 3 factor.
def check_factors(factors, n) :
    factors = filter(lambda x: len(str(x)) == 3, factors)
    for i in factors:
        if(len(str(n/i)) == 3):
            print i, n/i
            return True

for i in xrange(N, 100 * 100, -1):
    if palindrome(i) and check_factors(factors(i), i):
        print 'Biggest Palindrome is  ', i
        break;

