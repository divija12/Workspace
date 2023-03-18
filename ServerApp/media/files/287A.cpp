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
vector<string> v;
f(i,4)
{
    st s;
    cin>>s;
    v.push_back(s);
}
f(i,3)
{
    f(j,3)
    {
        if(v[i][j]==v[i+1][j] && v[i][j]==v[i][j+1])
        {
            cout<<"YES";
            return;
        }
        if(v[i][j]==v[i+1][j] && v[i][j]==v[i+1][j+1])
        {
            cout<<"YES";
            return;
        }
        if(v[i][j]==v[i][j+1] && v[i][j]==v[i+1][j+1])
        {
            cout<<"YES";
            return;
        }
        if(v[i+1][j+1]==v[i+1][j] && v[i+1][j+1]==v[i][j+1])
        {
            cout<<"YES";
            return;
        }

    }
}
cout<<"NO";
}

int main()
{
ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
cout<<setprecision(19);
// ll t;cin>>t;while(t--)
solve();
return 0;
}