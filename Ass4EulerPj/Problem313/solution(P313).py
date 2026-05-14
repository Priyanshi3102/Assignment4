# Project Euler Problem 313
# Sliding Game

from math import isqrt

LIMIT = 10**6

# Generate primes using Sieve of Eratosthenes
is_prime = [True] * (LIMIT + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, isqrt(LIMIT) + 1):
    if is_prime[i]:
        for j in range(i * i, LIMIT + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, LIMIT + 1) if is_prime[i]]

total = 0

for p in primes:
    p_square = p * p
    total += (p_square - 1) // 24

answer = total * 2

print("Answer:", answer)