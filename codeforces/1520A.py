for _ in range(int(input()):
    num = int(input())
    s = input()
    ans = "YES"
    for i in range(1,len(s)):
        if s[i] in s[:i] and s[i] != s[i-1]:
            ans = "NO"
    print(ans)
