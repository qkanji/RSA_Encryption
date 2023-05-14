import math
import time

# n = 2**1024
n = int(input("max: "))

start = time.time()
A = [False, False]
A.extend([True for i in range(n - 2)])
print("created A")
for i in range(2, math.ceil(math.sqrt(n)) + 1):
    if A[i]:
        print(i)
        i2 = i*i
        k = [i2, i2+i]
        k.extend([i2+x*i for x in range(2, n) if i2+x*i <= n])
        for j in k:
            try:
                A[j] = False
            except IndexError:
                break
end = time.time()

print([i for i in range(len(A)) if A[i]])
print(end - start)
