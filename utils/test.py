from quadratic_congruence import legendre, solve_quadratic
from lfsr import self_shrinking_lfsr

q = 10
p = 13

try:
  print(f"Testing Legendre function: legendre({q}) mod {p} is: {legendre(q,p)}")
except Exception as error:
  print(f"Error with legendre function:\n {error}")

try:
  print(f"Testing quadratic solver function: square root of {q} mod {p} is: {solve_quadratic(q,p)}")
except Exception as error:
  print(f"Error with solve_quadratic function:\n {error}")

tap = int('1000001010011', 2) # primitive tap polynomial of length 12
fill = int('101001011010', 2) # random fill bitstring of length 12
try:
  print("Testing self_shrinking lfsr:")
  print(f"  Initializing with tap = {format(tap, 'b')} and fill = {format(fill, 'b')}")
  ss = self_shrinking_lfsr(tap, fill)
  print("  First 100 bits generated:")
  print(" ", ''.join([str(next(ss)) for i in range(100)]))
except Exception as error:
  print(f"Error with self_shrinking_lfsr function:")
  raise error