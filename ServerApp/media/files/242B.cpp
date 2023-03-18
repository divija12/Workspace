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
ll n;
cin>>n;
vector<pi> v,ans;
f(i,n)
{
    ll x,y;
    cin>>x>>y;
    v.push_back({x,y});
}
sort(v.begin(),v.end());
while(v.size()!=1)
{
    ll m=v.size();
    for(ll i=0;i<m-1;i+=2)
    {
        if(v[i].first<=v[i+1].first && v[i].second<=v[i+1].second)
        {
            v[i]={v[i].first,v[i+1].second};
            v.erase(find(v.begin(),v.end(),i+1));
        }
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