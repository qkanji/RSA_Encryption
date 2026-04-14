import math
import time

maximum = int(input("Enter maximum number to search for primes up to: "))

start = time.time()
A = [False, False]
A.extend([True for i in range(maximum - 2)])
print(f"Initialized sieve array of size {maximum}...")

# Implements the Sieve of Eratosthenes algorithm to find all primes up to a bounded limit.
# It iteratively marks the multiples of each identified prime as composite (False), starting from 2.
for i in range(2, math.ceil(math.sqrt(maximum)) + 1):
    if A[i]:
        i2 = i*i
        k = [i2, i2+i]
        k.extend([i2+x*i for x in range(2, maximum) if i2+x*i <= maximum])
        for j in k:
            try:
                A[j] = False
            except IndexError:
                break
end = time.time()

primes = [i for i in range(len(A)) if A[i]]
print(f"Found {len(primes)} primes in range.")
print(f"Time taken: {round(end - start, 4)} seconds")
