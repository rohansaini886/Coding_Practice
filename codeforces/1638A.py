for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split(' ')))
    a = 1
    arr = []
    if l == sorted(l):
        print(*l)
        continue
    for i in range(n):
        if a == l[i]:
            a += 1
        else:
            idx = l.index(a)
            arr = l[:i] + list(reversed(l[i:idx+1])) + l[idx+1:]
            break
    print(*arr)
