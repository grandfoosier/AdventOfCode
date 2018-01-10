# This routine finds the number of non-primes in [L, U, s]
# With a == 0, L = U = 84, and s = 17 (but that doesn't matter)
# With a == 1, L = 84*100 + 100000 = 108400, U = L + 17000 = 125400, s = 17

from sympy import isprime

h = 0
for i in range(108400, 125417, 17):
    if isprime(i) != True: h += 1
print "\n%i\n\n" % h
