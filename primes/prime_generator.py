from math import ceil, sqrt
from .prime_checker import test_prime

def erastosthenes(n):
  """
  Uses the Sieve of Erastosthenes to generate all primes < n.
  Returns a sorted list of the primes, starting at 2.
  """
  # Array of length n+1, initially holds 'True' for all integers 0-n
  array = [True for i in range(0,n+1)]
  # set 0 and 1 to False to begin with
  array[0] = False
  array[1] = False
  # Find sqrt(n), we only need to check numbers up to this point
  sqrt_n = int(ceil(sqrt(n)))
  # Start sieving, from 2 up to sqrt(n)
  for i in range(2,sqrt_n):
    # Start j at i^2
    j = i**2
    # while j + ik is still less than or equal to n:
    while (j <= n):
      # Set element array[j] to False, it's composite
      array[j] = False
      # increment j by i
      j = j + i
  
  # After sieving is complete, return everything in array that has value 'True.' These are primes.
  return [i for i in range(0,n) if array[i]]

def next_prime(n):
  """
  increments n until it hits a prime number, and returns it.
  """
  #set n to the next odd number
  n = n+1 if (n%2 == 0) else n+2
  while (True):
    if (test_prime(n)):
      return n
    n = n+2 # increment by 2 to skip the even numbers

def generate_primes(start=1, n=-1, stop=None):
  """
  This function returns a generator to obtain sequential prime numbers.
  For obtaining a list of primes with an upper bound,
  the erastosthenes function is better suited.
  Use this function when dealing with large primes, or no upper bound.
  Also, the erastosthenes function builds the entire array of primes in memory
  and returns it all at once, while this function returns a generator,
  and is more memory efficient.
  ---
  Optional parameters:
  start <int>: which number to start generating from.
  n <int>: how many primes to generate. Default is -1,
    meaning generator will run indefinitely.
  stop <int>: upper bound for generating primes.
    The last prime returned will be less than or equal to end.
  """
  count = 0
  last = start
  if(start == 1):
    yield 2
    last = 2
    count += 1
  
  while(count != n):
    last = next_prime(last)
    if (stop and last > stop):
      break
    count += 1
    yield last
