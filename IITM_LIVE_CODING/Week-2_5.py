def findUnion(set1, set2):
    x = list(set1)
    y = list(set2)
    z = []
    x = sorted(x)
    y = sorted(y)
    z = x + y
    z = set(z)
    return sorted(z)
    
set1 = [int(item) for item in input().split()]
set2 = [int(item) for item in input().split()]
print(*findUnion(set1, set2))
