"""
this file contains functions to solve quadratic congruences,
i.e. congruences of the form x^2 = q (mod p), where p is a prime.
""" 

def legendre(q, p):
    """
    checks to see if q is a quadratic residue modulo p, where p is prime.
    i.e. the quadratic congruence x^2 = q (mod p) has solutions
    
    returns 1 if true,
    -1 if false,
    0 if q = 0 (mod p)
    """
    if (q == 0):
        return 0
    
    return 1 if (pow(q, int((p-1)/2), p) == 1) else -1

def format_n(n):
    """
    this function takes a number n and writes it as n = d*2^s + 1, where d is odd and s >= 0
    d and s are returned
    """
    d = n
    s = 0
    # as long as d is still even, keep dividing by 2
    while (d%2==0):
        d = d >> 1 # halve d
        s = s + 1 # increment s

    return d, s

def solve_quadratic(q, p):
    """
    Given a prime p and integer q, 1 <= q < p, this function attempts to solve the
    quadratic congruence x^2 = q (mod p) for x, where 1 <= x < p.
    The other solution is -x (mod p)
    NOTE: this function assumes a solution exists.
    
    If p = 3 (mod 4), the function returns x = q^((p+1)/4) (mod p)
    if p = 1 (mod 4), the function uses the Tonelli-Shanks algorithm to find x.
    """
    # 2 is special case, handle it separately:
    if (p == 2):
        return q&1
    
    # if p = 3 (mod 4), we have an easy relation to find a solution
    if (p%4 == 3):
        return pow(q, int((p+1)/4), p)
    
    # Otherwise, if p = 1 (mod 4), use Tonelli-Shanks
    
    # write p-1 as d*2^s, where d is odd
    d, s = format_n(p-1)
    # find a z which is a quadratic NON-residue mod p
    z = 2
    while (legendre(z,p) == 1):
        z += 1
        
    # initialize our variables
    m = s
    c = pow(z, d, p)
    t = pow(q, d, p)
    x = pow(q, int((d+1)/2), p)
    
    # begin loop, trying to make t = 1
    while (t != 1):
        # find the least i, 0 < i < M, such that t^(2^i) = 1
        t2 = t
        i = 0
        while (t2 != 1):
            t2 = pow(t2, 2, p)
            i += 1
        # set b = c^(2^(m-i-1)) (mod p)
        b = pow(c, 1<<(m-i-1), p)
        m = i
        c = pow(b, 2, p)
        t = t*c % p
        x = x*b % p
        
    return x

