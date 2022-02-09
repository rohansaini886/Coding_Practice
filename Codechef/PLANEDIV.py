from collections import defaultdict
from fractions import gcd
def res():
    for _ in range(int(input())):
        n=int(input())
        s=defaultdict(set)
        for i in range(n):
            a,b,c=map(int,input().split())
            g=gcd(a,b)
            h=gcd(g,c)
            s[a/g,b/g].add((a/h,b/h,c/h))
        print(max(map(len,s.values())))
res()
