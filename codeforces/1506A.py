for s in[*open(0)][1:]:n,m,x=map(int,s.split());x-=1;print(x%n*m+x//n+1)
