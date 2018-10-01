from fractions import gcd

def pollard_rho(n):
    """
    This function returns one factor of n
    
    It utilizes the fact that if you use a function (in this case, g(x) = x^2 + 1) to generate
    pseudorandom integers in a closed modulo field, by the birthday paradox eventually you will
    hit a number you already hit before, and thus a cycle will begin.
    
    We know the sequence x_n in modulo field n, but we DON'T know the sequence x_d,
    which is x_n in modulo field d, where d is a factor of n.
    
    But according to the birthday paradox, if the sequence x_n runs long enough,
    its counterpart x_d will eventually hit a cycle. We detect this cycle using
    Floyd's cycle-finding algorithm.
    
    Usually, the cycle-finding algorithm operates on a known modulo, but we make it work here
    by using a single fact:
    if x_d1 = x_d2 (modulo d), that means x_d2 = x_d1 + d*k
    we don't know what x_d1 and x_d2 are, but we CAN find what d*k is, by going back to the
    original sequence, x_n, where x_n1 corresponds to x_d1 and x_n2 corresponds to x_d2.
    By taking the difference x_n2 - x_n1, we know that the result is of the form
    d*k. Now simply taking the gcd(x_n2 - x_n1, n), we should get the factor d.
    
    This test can potentially fail if x_n2 - x_n1 happens to equal n, in which case
    gcd(n, n) will return n, and not a factor of n. But this has a very low chance of happening,
    and if it does happen, we simply try a different starting value for x_n.
    """
    # initial value for x. x is Floyd's 'tortoise,' it moves to the next number
    # in the sequence one at a time.
    x = 2
    # initialize y at the same value as x. y is Floyd's 'hare,' it skips
    # every other term in the sequence, making it 'move' twice as fast as x
    y = x
    # initialize d to 1, if a factor is found d will hold it
    d = 1
    # define the function we're using to generate the sequence x_n
    # in this case, our function is x_n = (x_n-1)^2 + 1
    # i.e. each term is the previous term squared, plus one
    def g(a):
        return (pow(a,2,n) + 1) % n
    
    # Begin the cycle detection loop
    # as long as the gcd(y - x, n) is 1, a cycle has not been detected
    while (d == 1):
        x = g(x) # x takes the next value in x_n
        y = g(g(y)) # y takes the value AFTER the next in x_n
        d = gcd(abs(x - y), n) # calculate gcd(|x-y|, n) abs() since we don't know which one's bigger
        # if the counterparts of x and y in modulo d, x_d and y_d, are congruent (mod d),
        # then |x-y| will be some multiple of d, call it d*k. Since n is another multiple of d,
        # such as d*m, taking gcd(d*k, d*m) should give us the factor d.
        # of course, it's entirely possible that k and m themselves have common factors.
        # this is fine, then gcd(d*k, d*m) will just give us another factor of n besides d.
        # Either way, we're happy to have found a factor.
    
    # we return d, UNLESS we ran into the unfortunate case where |x-y| = n, in which case
    # gcd gives us n, giving us no new information.
    # here, we simply return None, but in a more robust implementation you would simply
    # try again with a different starting value for x.
    return d if (d != n) else None