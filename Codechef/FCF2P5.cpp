#include<bits/stdc++.h>
    #define int long long
    using namespace std;
    int32_t main()
    {
       ios_base::sync_with_stdio(false);cin.tie(NULL);    
       int n,q;
       cin>>n>>q;
     
       int a[n];
       int pos[n];
       for (int i = 0; i < n; ++i)
       {
       	cin>>a[i];
       	a[i]--;
       	pos[a[i]]=i;
       }
       int d[n];
       d[0]=0;
       for (int i=1; i < n; ++i )
       {
       	d[i]=d[i-1]+abs(pos[i-1]-pos[i]);
       }
     
       while(q--)
       {
       	int src,dest;
       	cin>>src>>dest;
       	src--,dest--;
       	cout<<(int)(abs(d[a[src]]-d[a[dest]]))<<'\n';
       }
     
     
     
       cerr<<"\n"<<(float)clock()/CLOCKS_PER_SEC*1000<<" ms"<<endl;
       return 0;
    } 
