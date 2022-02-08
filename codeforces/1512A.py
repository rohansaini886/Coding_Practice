for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split(' ')))
    if l.count(max(l)) == n - 1:
        print(l.index(min(l)) + 1)
    else:
        print(l.index(max(l)) + 1)
    
