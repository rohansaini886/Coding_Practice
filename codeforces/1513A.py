for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    l = []
    for i in range(1, n + 1):
        l.append(i)
    if n == k or (k >= n - k):
        print(-1)
    else:
        a = []
        for i in range(k):
            a.append(i + 1)
            a.append(n - i)
        a.extend(range(k + 1, n - k +1))
        print(*a)
