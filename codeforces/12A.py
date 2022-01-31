matrix = []
for i in range(3):
    s = input()
    matrix.append(list(s))
a = matrix
if a[0][0] == a[2][2] and a[0][1] == a[2][1] and a[0][2] == a[2][0] and a[1][0] == a[1][2]:
    print("YES")
else:
    print("NO")
