n = int(input())
l = list(map(int, input().split(" ")))
l.sort()
if n == 1 or l.count(min(l)) == n:
    print("NO")
else:
    print(l[l.count(min(l))])
