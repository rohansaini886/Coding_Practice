s = input()
r = input()
t = ""
for i in range(1, len(s) + 1):
    t += s[-i]
if r == t:
    print("YES")
else:
    print("NO")
