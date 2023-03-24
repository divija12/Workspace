#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define  vi vector<ll> 
#define  vs vector<char> 
#define  st string 
#define  pi pair<ll,ll> 
#define  si set<ll> 
#define  ss set<char> 
#define  mi map<ll,ll>  
#define  ms map<char,ll> 
typedef long double ld;
#define f(i,n) for(ll i=0;i<n;i++)
#define vp vector<pair<ll,ll>>
#define TxtIO   freopen('input.txt','r',stdin); freopen('output.txt','w',stdout);


void solve()
{
ll n;
cin>>n;
vector<string> v(n);
unordered_map<string,ll> m;
f(i,n)
{
    cin>>v[i];
}
f(i,n)
{
    if(m.count(v[i]))
    {
        if(m[v[i]])
        {
            m[v[i]]++;
            st a =to_string(m[v[i]]);
            cout<<v[i]+a<<endl;
        }
        else
        {
            m[v[i]]++;
            cout<<v[i]+'1'<<endl;
        }
        
    }
    else
    {
        cout<<"OK"<<endl;
        m.insert({v[i],0});
    }
}

}

int main()
{
ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
cout<<setprecision(19);
// ll t;cin>>t;while(t--)
solve();
return 0;
}