for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split(' ')))
    x = []
    flag = False
    for i in range(n):
        m = l[:i] + l[i+1:]
        x.append(sum(m)/(n-1))
    for i in range(n):
        if round(float(l[i]), 1) == x[i]:
            flag = True
            break
        else:
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")
