for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split(' ')))
    count = l.count(1) + l.count(3)
    print(count)
    
