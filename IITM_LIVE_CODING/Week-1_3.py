def shuffle(x, y):
    z = []
    for i in range(min(len(x), len(y))):
        z.append(x[i])
        z.append(y[i])
    if len(x) < len(y):
        z += y[len(x):]
    else:
        z += x[len(y):]
    return z
L1 = eval(input())
L2 = eval(input())
print(shuffle(L1,L2))
