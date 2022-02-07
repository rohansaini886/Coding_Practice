for _ in range(int(input())):
    a, b = map(int, input().split(" "))
    s = input()
    t = ""
    for i in range(1, a + 1):
        t += s[-i]
    s_1 = s + (t * b)
    s_2 = (t * b) + s
    if s_1 == s_2:
        print(1)
    else:
        print(2)
