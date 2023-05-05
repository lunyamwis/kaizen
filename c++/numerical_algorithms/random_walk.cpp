#include <bits/stdc++.h>
 
using namespace std;
 
const int mod = 998244353;
 
int main(){
    int n, s, t;
    cin >> n >> s >> t;
    s--, t--;
 
    vector < vector <int> > g(n);
    vector <int> previous(n, -1);
    vector <int> inPath(n);
    vector <long long> res(n);
 
    for (int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;
        a--, b--;
        g[a].push_back(b);
        g[b].push_back(a);
    }
 
    function <void (int, int)> dfs = [&] (int v, int p) {
        for (int to : g[v]) {
            if (to == p) continue;
            previous[to] = v;
            dfs(to, v);
        }
    };
 
    function <void (int, int, long long)> dfs2 = [&] (int v, int p, long long k) {
        res[v] = k * (long long)g[v].size();
        for (int to : g[v]) {
            if (to == p) continue;
            dfs2(to, v, k);
        }
    };
 
    dfs(s, -1);
 
    int ptr = t;
    inPath[t] = true;
 
    while (ptr != s) {
        res[previous[ptr]] = res[ptr] + 2;
        ptr = previous[ptr];
        inPath[ptr] = true;
    }
 
    for (int v = 0; v < n; v++) {
        if (inPath[v]) {
            res[v] = res[v] / 2 * (long long)g[v].size();
            for (int to : g[v]) {
                if (!inPath[to]) {
                    dfs2(to, v, res[v] / (int)g[v].size());
                }
            }
        }
    }
 
    res[t]++;
 
    for (long long i : res)
        cout << i % mod << ' ';
    cout<<'\n';
 
    return 0;
}