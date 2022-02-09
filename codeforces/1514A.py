import math
for tc in range(int(input())):
	n=int(input())
	li=list(map(int,input().split()))
	bb="NO"
	for i in li:
		if math.sqrt(i)!=math.isqrt(i):
			bb="YES"
	print(bb)
