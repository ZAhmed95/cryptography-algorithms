# The Naive Trial-Multiplication Algorithm for solving Discrete Log Problems
def dlp_naive(a, b, p):
    """
    This function solves the discrete log problem a^x = b (mod p) for x.
    ---
    It uses the naive approach of trial multiplication, checking every exponent until the congruence is satisfied.
    Note that this function assumes the modulus is prime, since the Euler function is calculated as p-1.
    """
    x = 0 # this holds the value of the exponent in the loop
    ax = 1 # this holds the value of a^x within the while loop
    order = p-1 # the Euler function of a prime p returns p-1
    while (ax != b):
        # the loop stops if a^x = b (the solution has been found)
        # if x > order, that means there is no solution
        if (x > order):
            return None
        # increment x
        x += 1 
        # calculate next power of a^x by multiplying by a, then take modulo p
        ax *= a
        ax %= p
    
    # if the loop properly finished, then x contains the value that satisifes a^x = b (mod p)
    return x
	
# define the values we want to solve for
p = 247457076132467 # the prime modulus
b = 184655036034450 # the power
a = 2 # the base
import time
t = time.time() # for timing purposes
#compute discrete log
x = dlp_naive(a,b,p)
print ("x = " + str(x))
print ("time taken: " + str(time.time()-t) + " seconds")