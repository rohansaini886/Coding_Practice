import math

for _ in range(int(input())):
    n = int(input())
    s = str(n)
    while math.gcd(n,sum(map(int,str(n)))) < 2:
        n += 1
    print(n)
