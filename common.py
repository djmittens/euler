# Common functions that may be used by other problems.

##
# Return a list of factors for the given number
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

##
# Check for primeness of a number
def prime(num):
    if num == 1:
        return False
    if len(factors(num)) > 2:
        return False
    return True
