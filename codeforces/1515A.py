def f(n,d,l):
	for i in range(1,n):
		if sum(l[:i])==d:
			l[i-1],l[i]=l[i],l[i-1]
	if sum(l)==d:
		 print("NO")
	else:
		print("YES")
		print(*l)
 
for i in range(int(input())):
	n,d=input().split()
	n=int(n)
	d=int(d)
	l=list(map(int,input().split()))
	f(n,d,l)
