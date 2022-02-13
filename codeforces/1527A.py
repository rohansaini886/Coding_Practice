for _ in range(int(input())):
    s = int(input())
    while s & s - 1:
        s -= 1
    print(s-1)
