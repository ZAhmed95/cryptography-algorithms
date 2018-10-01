"""
Contains miscellaneous utility functions
"""
import math

def digits(n, b=10):
    """
    Returns the digits of n in base b
    """
    # NOTE: due to precision errors, this function may not be fully accurate for very large numbers (>~47 bits)
    return int(math.floor(math.log(n, b))+1)

def xor_all(bits):
    # xors every bit in input bitstring with each other, and returns the result
    result = 0
    while (bits != 0):
        result = result ^ (bits&1)
        bits = bits >> 1
    return result

def read_from_file(file_name):
  """
  returns iterator that loops through each line of file, returning the integer on that line
  """
  with open(file_name, 'r') as f:
    for l in f:
      yield int(l[0:len(l)-1])