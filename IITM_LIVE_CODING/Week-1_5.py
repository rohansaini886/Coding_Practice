def sumsquare(l):
    odd = []
    even = []
    for i in l:
        if i % 2 == 0:
            even.append(i ** 2)
        else:
            odd.append(i ** 2)
    return [sum(odd), sum(even)]
L = eval(input())
print(sumsquare(L))
