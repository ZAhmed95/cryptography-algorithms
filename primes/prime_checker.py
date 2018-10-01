from random import randint

def fermat_test(n):
  """
  A simpler test for primes than miller-rabin. if 2^(n-1) = 1 (mod n), returns True, else False.
  """
  return pow(2,n-1,n) == 1

def miller_rabin(n, k=32):
  """
  this function tests a number n to see if it's prime or composite.
  
  Input Parameters:
  ---
  n: the integer to check for primality
  k: an integer representing the number of bases that will be checked.
      higher values of k will cause the function to take longer, but result
      in greater certainty of primality.
  """
  
  def format_n(n):
    """
    this function takes a number n and writes it as n = d*2^s + 1, where d is odd and s >= 0
    d and s are returned
    """
    d = n - 1
    s = 0
    # as long as d is still even, keep dividing by 2
    while (d%2==0):
      d = d >> 1 # halve d
      s = s + 1 # increment s

    return d, s
  
  # represent n-1 as d*2^s
  d, s = format_n(n)
  
  # run k different witness trials
  for i in range(0,k):
    # choose a random witness between 2 (inclusive) and n-1 (exclusive)
    a = randint(2, n-2)
    # calculate x = a^d (mod n)
    x = pow(a, d, n)
    # if x = 1 or -1 (mod n), it satisfies the conditions for n to be prime
    if (x == 1 or x == n-1):
      continue # move on to the next witness
        
    # start repeatedly squaring x until we hopefully hit -1 (mod n)
    condition_met = False # boolean to check whether -1 is ever hit during the squaring process
    for r in range(1, s):
      x = pow(x, 2, n) # square x
      #if x becomes -1, we've satisfied condition 2, go to next witness
      if (x == n-1):
        condition_met = True
        break
      # if x becomes 1 WITHOUT ever hitting -1, that means x was a nontrivial square root
      # modulo n, which confirms n is composite
      if (x == 1):
        return False
    # if the above loop ended without ever hitting -1, then n cannot be prime
    if (not condition_met):
      return False
    # otherwise, continue with next witness
      
  # all witness trials successfully ended without the program ever returning false
  # this means n is probably prime
  return True

def test_prime(n, k=32):
  """
  A compound test for primality. First, the simpler and faster Fermat test is done.
  If the Fermat test returns false, then no further testing is needed, n is composite.
  If Fermat returns true, then we move to the more accurate Miller-Rabin test,
  using k iterations.
  """
  # Fermat test fails for n=2, and n=3 causes problem in MR's random witness generation,
  # so we handle these trivial cases here
  if (n == 2 or n == 3):
      return True

  # Try Miller-Rabin only if Fermat returned true, otherwise it's guaranteed composite
  return miller_rabin(n, k) if fermat_test(n) else False