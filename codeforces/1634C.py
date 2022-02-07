for _ in range(int(input())):
    n, k = map(int, input().split(" "))
    l = []
    if (n == k and n % 2 == 0 and k % 2 == 0) or k == 1 or n % 2 == 0:
        print("YES")
        for i in range(1, n + 1):
            temp =[]
            for j in range(i, n * k + 1, n):
                temp.append(j)
            l.append(temp)
        for i in l: 
            print(*i)  
    else:
        print("NO")
        continue
