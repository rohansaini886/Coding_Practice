for _ in range(int(input())):
    n = int(input())
    if n < 10:
        print(n)
    else:
        count = 9
        # s = str(n)
        while(n>10):
            s = str(n)
            if int((s[0] * len(s)), 10) <= n:
                count += int(s[0], 10)
                n =  int('9' * (len(s) - 1), 10)
            else:
                count += int(s[0], 10) - 1
                n =  int('9' * (len(s) - 1), 10)
                
        print(count)
