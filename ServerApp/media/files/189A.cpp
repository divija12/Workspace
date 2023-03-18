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
ll dp[4000];

ll maxno(ll n,ll a,ll b,ll c)
{
    if(n==0)
    return 0;
    if(n==a || n==b || n==c)
    return 1;
    return maxno(n-)
}
void solve()
{
ll n,a,b,c;
cin>>n>>a>>b>>c;
f(i,4000)
dp[i]=-1;



}

int main()
{
ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
cout<<setprecision(19);
// ll t;cin>>t;while(t--)
solve();
return 0;
}