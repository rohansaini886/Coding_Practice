for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split(' ')))
    l.sort()
    q = []
    for i in range(n):
        q.append(l[i])
        q.append(l[-i-1])
    print(*q)
