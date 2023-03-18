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
vi a(3*n);
f(i,3*n)
cin>>a[i];
int b=0,c=0,d=0;
for(int i=0;i<3*n-2;i+=3)
{
    b+=a[i];
}
for(int i=1;i<3*n-1;i+=3)
{
    c+=a[i];
}
for(int i=2;i<3*n;i+=3)
{
    d+=a[i];
}
if(d || b || c)
cout<<"NO";
else
cout<<"YES";


}

int main()
{
ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
// ll t;cin>>t;while(t--)
solve();
return 0;
}