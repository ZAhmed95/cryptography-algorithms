import math

def read_from_file(file_name):
    """
    returns iterator that loops through each line of file, returning the integer on that line
    """
    with open(file_name, 'r') as f:
        for l in f:
            yield int(l[0:len(l)-1])

def brute_factor(n):
    """
    This function computes the prime factorization of n, using brute force.
    
    It performs trial division by primes, which are read from an external file
    """
    # BASE CASE 1: factor of 1 is just 1, not included in prime factorization
    if (n == 1): return [1]
    
    # LOOP CASE:
    # once we find a factor, we divide it out and repeat the loop on the other factor
    # until no more factors can be found
    prime_factors = [] # list to hold all prime factors, from least to greatest
    sqrt_n = math.sqrt(n) # calculate sqrt(n)
    for d in read_from_file('primes.txt'):
        if (d > sqrt_n): break
        # while d is a factor of n:
        while (n%d == 0):
            # factor found, add to list
            prime_factors += [d]
            # return d, n/d
            # take out d from n
            n /= d
            # recalculate sqrt(n)
            #sqrt_n = math.sqrt(n)
    
    # END LOOP:
    # if n hasn't been reduced to 1 yet,
    # it's the last remaining prime factor
    if (n != 1): prime_factors += [n]
    
    # return the list
    return prime_factors