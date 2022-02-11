for _ in range(int(input())):
    x, y , k = map(int, input().split(' '))
    if x * y - 1 == k:
        print("YES")
    else:
        print("NO")  
