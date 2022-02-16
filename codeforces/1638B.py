for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    o,e = [],[]
    for i in arr:
        if i%2!=0:
            o.append(i)
        else:
            e.append(i)
    te,to = e[::],o[::]
    te.sort()
    to.sort()
    if te==e and to==o:
        print('Yes')
    else:
        print('No')
