# Cryptography Algorithms

A collection of functions useful in certain cryptographic applications.

## List of Algorithms

### Primality checking

Found in primes/prime_checker.py

Algorithms include:

- [Fermat test](https://en.wikipedia.org/wiki/Fermat_primality_test): a simple and very fast primality test, with good success rate
- [Miller Rabin](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test): slower than Fermat, but extremely reliable

### Prime generation

Found in primes/prime_generator.py

Algorithms include:

- [Sieve of Erastosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes): the classic method

### Discrete Log Problems

Found in discrete_log_problems/

Algorithms include:

- Naive approach: using trial and error
- [Baby Step Giant Step](https://en.wikipedia.org/wiki/Baby-step_giant-step): a more efficient approach using a meet-in-the-middle attack

### Integer Factorization

Found in integer_factorization/

Algorithms include:

- Brute Factorization: testing if the input number n is divisible by any prime up to sqrt(n)
- [Pollard Rho](https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm): an algorithm that excels at finding small factors quickly. Algorithm is explained in detail in the docstring for the function, in integer_factorization/pollard_rho/pollard_rho.py
- [Fermat Factorization](https://en.wikipedia.org/wiki/Fermat%27s_factorization_method) (*Coming soon!*): an algorithm that utilizes the fact that all odd integers can be represented as the difference of two squares.
- [Dixon Factorization](https://en.wikipedia.org/wiki/Dixon%27s_factorization_method) (*Coming soon!*): an algorithm that builds on Fermat's algorithm. Details in the docstring.
- [Quadratic Sieve](https://en.wikipedia.org/wiki/Quadratic_sieve) (*Coming soon!*): an algorithm that builds on Dixon's method. Details in the docstring.

### Miscellaneous and/or Utility Functions

Found in utils/

Algorithms include:

- [Self-Shrinking Linear Feedback Shift Register](https://en.wikipedia.org/wiki/Self-shrinking_generator): a pseudorandom bitstream generator, useful for stream ciphers (e.g. encrypting video streaming, voice chat, etc.)
- Digit Counter (found in utils/misc.py): given an input integer n and an optional base b, this function returns how many digits n has in base b.
- [Legendre Checker](https://en.wikipedia.org/wiki/Legendre_symbol) (Found in utils/quadratic_congruence.py): returns the Legendre symbol of an integer q modulo a prime p. Details in the docstring.
- Quadratic Congruence Solver (Found in utils/quadratic_congruence.py): given a quadratic residue q in modulo a prime p, returns the square root of q (mod p). In the case that p ≡ 1 (mod 4), the square root is easy to find (see docstring for details). In the case that p ≡ 3 (mod 4), the function resorts to the [Tonelli-Shanks Algorithm](https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm) to find the root.