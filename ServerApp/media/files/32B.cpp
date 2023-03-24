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


void solve()
{
st s;
cin>>s;
vi v;
int n=s.size(),i=0;
while(i<n)
{
    if(s[i]=='.'){
    v.push_back(0);
    i++;}
    else
    {
        if(s[i+1]=='.')
        v.push_back(1);
        else
        v.push_back(2);
        i+=2;
    }
}
f(i,v.size())
cout<<v[i];


}

int main()
{
ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
// ll t;cin>>t;while(t--)
solve();
return 0;
}