# The Baby-Step Giant-Step algorithm for solving Discrete Log Problems
import math
def dlp_bsgs(a,b,p):
    """
    This function solves the discrete log problem a^x = b (mod p) for x.
    ---
    It uses the Baby-Step Giant-Step algorithm developed by Shanks.
    The desired exponent x is written as x = im + j, where m = ceil(sqrt(n)),
    and i and j can take values from 0 to m-1.
    We try to find values of i and j that satisifes ((a^-m)^i)b = a^j
	If successful, we calculate x = im + j and return x
    """
    # since p is prime, the order of the group, n, is p-1
    n = p-1
    # calculate m, m = ceil(sqrt(n))
    m = int(math.ceil(math.sqrt(n)))
    #compute and store all values of a^j
    aj_dict = {} # stores all m values for a^j, where key: a^j, value: j
    aj = 1 # stores successive values of a^j for the loop, starting at a^0
    for j in range(0,m):
        # store the (key : value) pair (a^j : j)
        aj_dict[aj] = j
        # calculate the next value of a^j
        aj *= a
        aj %= p
        
    # calculate a^-1 (a inverse) mod p
    # since p is prime, we know that a^(p-2) = a^-1 (mod p), since a^(p-1) = 1 (mod p)
    a_inv = pow(a, p-2, p) # pow() uses square-and-multiply for modular exponentiation
    # now calculate a_inv^m
    a_invm = pow(a_inv, m, p)
    
    y = b # y will hold the value of b(a^-m)^i
    for i in range(0,m):
        # check to see if y is in the aj_dict
        if y in aj_dict:
            # if it is, we've found our values for i and j.
            # get j
            j = aj_dict[y]
            # compute x = im + j, and return it
            x = i * m + j
            return x
        # otherwise, calculate the next value of y
        y *= a_invm
        y %= p
    
    #if this loop finishes without returning, no solution was found. Function returns None.
    
# define the values we want to solve for
p = 247457076132467 # the prime modulus
b = 184655036034450 # the power
a = 2 # the base
import time
t = time.time() # for timing purposes
#compute discrete log
x = dlp_bsgs(a,b,p)
print ("x = " + str(x))
print ("time taken: " + str(time.time()-t) + " seconds")