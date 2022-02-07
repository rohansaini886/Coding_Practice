for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split(" ")))
    a = []
    l.sort()
    s = set(l)
    s = sorted(s)
    for i in s:
        l.pop(l.index(i))
        a.append(i)
    for i in range(len(l)):
        for j in l:
            if l.count(j) != 1:
                a.append(j)
                l.pop(l.index(j))
                break
            else:
                a.append(j)
                l.pop(l.index(j))
    print(*a)
