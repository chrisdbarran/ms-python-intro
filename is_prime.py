import numpy as np
import matplotlib.pyplot as plt

def is_prime(p):
    if p == 2 or p ==3: return True
    if p < 2 or p%2 == 0: return False
    if p < 9: return True
    if p%3 == 0: return False

    i = 5
    while i*i <= p:
        if (p%i == 0 or p%(i+2) == 0 ): return False
        i += 6

    return True


primes = []
ns     = []

n_max = 200000
num_bins = 120
for n in range (2, n_max, 1):
    p = 6*n

    if is_prime(p - 1):
        print(f"n: {n}, p: {p - 1}")
        ns.append(n)
        primes.append(p - 1)

    if is_prime(p + 1):
        print(f"n: {n}, p: {p + 1}")
        ns.append(n)
        primes.append(p + 1)
    

print(len(primes))
print(max(primes))

plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})
plt.hist(primes, bins=num_bins)
plt.gca().set(title='Frequency of primes', ylabel='Frequency')
plt.show()