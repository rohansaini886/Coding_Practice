import sys

sys.setrecursionlimit(10**8)

for _ in range(int(input())):
    s=input()
    dic={}
    def do(ini,se):
        index,ma,mi,sign=ini+1,0,0,True
        
        while se[index]!=')':
            char=se[index]
            if char=='?':
                if sign:ma+=1
                else:mi+=1
            elif char=='+' :sign=True
            elif char=='-' :sign=False
            elif char=='(' :
                arr=do(index,se)
                if sign:
                    ma+=arr[0]
                    mi+=arr[1]
                else:
                    ma+=arr[1]
                    mi+=arr[0]
                index=arr[2]
            index=index+1
        dic[ini]=ma
        return [ma,mi,index]
        
    do(0,s)
    
    
    ques=int(input())
    res=[]
    for __ in range(ques):
        ini,fin=map(int,input().split())
        if ini==fin:res.append(1)
        else:res.append(dic[ini-1])
    print(*res)    
                    
