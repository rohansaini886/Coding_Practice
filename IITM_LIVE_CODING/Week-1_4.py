def expanding(l):
    z = []
    for i in range(1, len(l) - 1):
        diff = abs(l[i] - l[i + 1])
        z.append(diff)
    count = 0
    for i in z:
        count += z.count(i)
    if z != sorted(z) or count != len(z):
        return False
    return True
    
L = eval(input())
print(expanding(L))
