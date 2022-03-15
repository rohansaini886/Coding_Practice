import math
def prime_product(n):
    primes = []
    for i in range(2, n + 1):
        temp = []
        for j in range(2, i + 1):
            #print(i, j)
            if i % j == 0:
                temp.append(j)
        if len(temp) == 1:
            primes.append(i)
    #print(primes)
    for prime in primes:
        for prime_ in primes:
            if prime * prime_ == n:
                return True
    return False
n = int(input())
print(prime_product(n))
