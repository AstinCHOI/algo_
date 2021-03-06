#include <bits/stdc++.h>
// #include "testlib.h"  
using namespace std ;

#define ft first
#define sd second
#define pb push_back
#define all(x) x.begin(),x.end()

#define ll long long int
#define vi vector<int>
#define vii vector<pair<int,int> >
#define pii pair<int,int>
#define plii pair<pair<ll, int>, int>
#define piii pair<pii, int>
#define viii vector<pair<pii, int> >
#define vl vector<ll>
#define vll vector<pair<ll,ll> >
#define pll pair<ll,ll>
#define pli pair<ll,int>
#define mp make_pair
#define ms(x, v) memset(x, v, sizeof x)

#define sc1(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d%d",&x,&y)
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z)

#define scll1(x) scanf("%lld",&x)
#define scll2(x,y) scanf("%lld%lld",&x,&y)
#define scll3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z)

#define pr1(x) printf("%d\n",x)
#define pr2(x,y) printf("%d %d\n",x,y)
#define pr3(x,y,z) printf("%d %d %d\n",x,y,z)

#define prll1(x) printf("%lld\n",x)
#define prll2(x,y) printf("%lld %lld\n",x,y)
#define prll3(x,y,z) printf("%lld %lld %lld\n",x,y,z)

#define pr_vec(v) for(int i=0;i<v.size();i++) cout << v[i] << " " ;

#define f_in(st) freopen(st,"r",stdin)
#define f_out(st) freopen(st,"w",stdout)

#define fr(i, a, b) for(i=a; i<=b; i++)
#define fb(i, a, b) for(i=a; i>=b; i--)
#define ASST(x, l, r) assert( x <= r && x >= l )

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

const int mod = 1e9 + 7;

int ADD(int a, int b, int m = mod) {
    int s = a;
    s += b;
    if( s >= m )
      s -= m;
    return s;
}

int MUL(int a, int b, int m = mod) {
    return (1LL * a * b % m);
}

int power(int a, int b, int m = mod) {
    int res = 1;
    while( b ) {
        if( b & 1 ) {
            res = 1LL * res * a % m;
        }
        a = 1LL * a * a % m;
        b /= 2;
    }
    return res;
}

ll nC2(ll x) {
    return ( x * ( x - 1 ) / 2 );
}

const int maxn = 5 * 1e5 + 5;
vi adj[ maxn ];
vii g[ maxn ];
int in[ maxn ], out[ maxn ], L[ maxn ], n, q, LCA[ maxn ][ 22 ], lg, vis[ maxn ], sz[ maxn ];

void dfs() {

    queue<int> Q;
    Q.push(1);
    vis[1] = 1;
    stack<int> S;
    while( !Q.empty() ) {
        int u = Q.front(); Q.pop();
        sz[u] = 1;
        S.push(u);
        for( auto it: adj[u] ) {
            if( !vis[it] ) {
                vis[ it ] = 1;
                L[it] = L[u] + 1;
                LCA[it][0] = u;
                Q.push(it);
            }
        }
    }

    while( !S.empty() ) {
        int u = S.top(); S.pop();
        vis[u] = 0;
        for( auto it: adj[u] ) {
            if( !vis[it] )
                sz[u] += sz[it];
        }
    }

    Q.push(1);
    in[1] = 1; 
    vis[1] = 1;
    while( !Q.empty() ) {
        int u = Q.front(); Q.pop();
        S.push(u);
        int s = 0;
        for( auto it: adj[u] ) {
            if( !vis[it] ) {
                vis[it] = 1;
                in[it] = s + in[u] + 1;
                s += sz[it]; 
                Q.push(it);
            }
        }
    }

    while( !S.empty() ) {
        int u = S.top(); S.pop();
        vis[u] = 0;
        out[u] = in[u];
        for( auto it: adj[u] ) {
            if( !vis[it] ) {
                out[u] = max(out[u], out[it]);
            }
        }
    }   
}

int getLca(int x, int y) {
    if(L[x] < L[y])
        swap(x, y);
    for(int i=lg; i>=0; i--) {
        if( LCA[x][i] != 0 && L[LCA[x][i]] >= L[y] )
            x = LCA[x][i];
    }
    if( x == y )
        return x;
    for(int i=lg; i>=0; i--) {
        if( LCA[x][i] != 0 && LCA[x][i] != LCA[y][i] )
             x = LCA[x][i] , y = LCA[y][i];
    }
    return LCA[x][0];
}

void ConstructLCA( int n ) {
    lg = ceil(log2(n));
    dfs();
    int i, j;
    fr(i, 1, lg) {
        fr(j, 1, n) {
            if(LCA[j][i-1]) {
                LCA[j][i] = LCA[LCA[j][i-1]][i-1];
            }
        }
    }
}

ll dp[2][ maxn ], ans, lev[ maxn ];
bool check[ maxn ];
void solve(int u) {
    queue<int> Q;
    Q.push(u);
    vis[u] = 1;
    lev[u] = 0;
    stack<int> S;
    while( !Q.empty() ) {
        u = Q.front(); Q.pop();
        S.push(u); 
        for( auto it: g[u] ) {
            if( !vis[it.ft] ) {
                vis[ it.ft ] = 1;
                lev[ it.ft ] = lev[ u ] + it.sd;
                Q.push(it.ft);
            }
        }
    }

    while( !S.empty() ) {
        u = S.top(); S.pop();
        vis[u] = 0;
        dp[0][u] = check[u] ? u : 0; 
        dp[1][u] = check[u] ? 1LL * lev[u] * u : 0;
        dp[1][u] %= mod;
        ll s = 0; 
        for( auto it: g[u] ) {
            if( !vis[it.ft] ) {
                s += dp[0][it.ft];
                if( s >= mod ) s -= mod;
                dp[0][u] += dp[0][it.ft];
                if( dp[0][u] >= mod ) dp[0][u] -= mod;
                dp[1][u] += dp[1][it.ft];
                if( dp[1][u] >= mod ) dp[1][u] -= mod;  
            }
        }
        // ok 
        for( auto it: g[u] ) {
            if( !vis[it.ft] ) {
                ans += 1LL * (dp[1][it.ft] - 1LL * dp[0][it.ft] * lev[u] % mod ) * (s - dp[0][it.ft]) % mod;
                if( ans >= mod ) ans -= mod;
                if( ans < 0 ) ans += mod;   
            }
        }
        if( check[u] ) ans += 1LL * (dp[1][u] - 1LL * lev[u] * dp[0][u] % mod ) * u % mod;
        if( ans >= mod ) ans -= mod;
        if( ans < 0 ) ans += mod;
    }
}

bool anc(int p, int u) {
    return in[p] <= in[u] && out[p] >= out[u];
}

int main() {
    cin >> n >> q;
    int i; fr(i, 1, n-1) {
        int u, v; cin >> u >> v;
        adj[u].pb( v );
        adj[v].pb( u );
    }
    ConstructLCA(n);
    int cnt = 0;
    while( q-- ) {
        int k;
        cin >> k; vii Q;
        set<int> K;
        fr(i, 1, k) {
            int x; cin >> x;
            check[x] = 1; 
            if(K.find(x) == K.end()) {
                K.insert(x);
                Q.pb(mp(in[x], x));
            }
        }
        k = Q.size();
        sort(all(Q));
        fr(i, 0, k-2) {
            int lca = getLca(Q[i].sd , Q[i+1].sd);
            if(K.find(lca) == K.end()) {
                K.insert(lca);
                Q.pb(mp(in[lca], lca));
            }
        }
        sort(all(Q));
        stack<int> s;s.push(Q[0].sd);
        for(i=1;i<Q.size();i++){
            while(!anc(s.top(),Q[i].sd)) s.pop();
            g[s.top()].pb({Q[i].sd, L[Q[i].sd] - L[s.top()]});
            g[Q[i].sd].pb({s.top(), L[Q[i].sd] - L[s.top()]});
            s.push(Q[i].sd);
        }
        ans = 0; solve(Q[0].sd);
        cout << ans << "\n";
        for( auto it: Q ) {
            g[it.sd].clear();
            dp[0][it.sd] = dp[1][it.sd] = lev[it.sd] = check[it.sd] = 0;
        }
        assert( ans >= 0 );
    }
    return 0;
}