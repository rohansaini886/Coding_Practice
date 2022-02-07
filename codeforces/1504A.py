for i in range(int(input())):
	l=input()
	l1=l+"a"
	l2="a"+l
	if l1!=l1[::-1]:
		print("YES")
		print(l1)
	elif l2!=l2[::-1]:
		print("YES")
		print(l2)
	else:
		print("NO")
