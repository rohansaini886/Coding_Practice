for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split(' ')))
    ans = 0
    for i in range(n):
        ans += (i + 1) * (n - i)
        if l[i] == 0:
            ans += (i + 1) * (n - i)
    print(ans)
