for _ in range(int(input())):
    n, x, y = map(int, input().split(" "))
    l = list(map(int, input().split(" ")))
    total = x + y + sum(l)
    if total % 2 == 0:
        print("Alice")
    else:
        print("Bob") 
