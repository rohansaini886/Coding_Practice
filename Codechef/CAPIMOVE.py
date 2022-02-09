t= int(input()) 

while(t):
    n= int(input())
    
    p=[[int(i)] for i in input().split()]
    for i in range (n):
        p[i].append(i+1)
    p.sort()
    p.reverse()
    
    connected=[]
    for i in range(n+1):
        connected.append([])
    
    for i in range(n-1):
        v, u= [int(i) for i in input().split()]
        connected[v].append(u)
        connected[u].append(v)
    
    final= []
    
    for i in range(1, n+1):
        infected= connected[i]
        ans= 0
        
        for j in p:
            if(j[1] != i and j[1] not in infected):
                ans= j[1]
                flag= 1
                break
        
        final.append(ans)
    
    print(*final)
    t -= 1
