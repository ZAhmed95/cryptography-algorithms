"""
Testing the prime checker function, test_prime()
This function uses two methods to test for primality:
First, it uses the extremely fast Fermat test.
If the Fermat test returns false, the number is guaranteed composite,
no further testing is needed.
If the Fermat test returns true, there is still the chance of
a false positive, so the function then applies the more reliable,
but also more expensive, Miller-Rabin test.
"""
from .prime_checker import test_prime
from .prime_generator import erastosthenes, next_prime, generate_primes

tests = [
  13, # prime
  48, # composite
  2668129, # prime
] # add your own test cases

print()
print("Testing primality:")
for p in tests:
  print(f"{p} is prime? {test_prime(p)}")

print()
print("Testing prime generation:")

print()
print("All primes under 100 generated by erastosthenes():")
print(erastosthenes(100))

print()
print("All primes under 100 generated by generate_prime():")
print([p for p in generate_primes(stop=100)])