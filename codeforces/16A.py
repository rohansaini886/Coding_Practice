a,b=map(int,input().split());c="a"
for i in range(a):
    z=input()
    if  c in z :print("NO");exit()
    if z.count(z[0])!=b:print("NO");exit()
    c=z[0]
print("YES")
