def findPair(l, x):
    l = sorted(l)
    n = len(l)
    for i in range(n):
        for j in range(i + 1, n):
            if l[i] + l[j] == x:
                return True
    return False
L = [int(item) for item in input().split()]
pairsum = int(input())
print(findPair(L, pairsum))
