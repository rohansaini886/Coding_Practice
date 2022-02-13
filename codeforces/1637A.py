for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split(' ')))
    if l == sorted(l):
        print("NO")
    else:
        print("YES")
