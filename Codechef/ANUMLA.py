for _ in range(int(input())):
    n=int(input())
    n2=2**n
    sums=[]
    ans=[]
    rem={}
    a=list(map(int,input().split()))
    a.sort()
    for i in range(1,n2):
        if a[i] in rem and rem[a[i]]!=0:
            rem[a[i]]-=1
        else:
            temp=[]
            for j in sums:
                temp.append(j+a[i])
            for j in ans:
                temp.append(j+a[i])
            for j in temp:
                if j not in rem:
                    rem[j]=0
                rem[j]+=1
                sums.append(j)
            ans.append(a[i])
            if len(ans)==n:
                break
    print(*ans)
