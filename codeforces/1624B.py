for _ in range(int(input())):
    # n = int(input())
    a, b, c = (map(int, input().split(' ')))
    if (((2*b-c)%a==0) and (2*b > c)) or (((2*b-a)%c==0) and (2*b > a)) or ((c+a)%(2*b)==0):
        print("YES")
    else:
        print("NO")
