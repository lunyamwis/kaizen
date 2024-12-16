from sys import setrecursionlimit
import threading
mod = 998244353

def random_walk():
    n, s, t = map(int, input().split())
    s -= 1
    t -= 1
    
    g = [[] for i in range(0, n)]
    previous = [-1 for i in range(0, n)]
    inPath = [False for i in range(0, n)]
    res = [0 for i in range(0, n)]
    
    for i in range(0, n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    
    def dfs(v, p):
        for to in g[v]:
            if to == p:
                continue
            previous[to] = v
            dfs(to, v)
    
    def dfs2(v, p, k):
        res[v] = k * len(g[v])
        for to in g[v]:
            if to == p:
                continue
            dfs2(to, v, k)
    
    dfs(s, -1)
    
    ptr = t
    inPath[t] = True
    
    while ptr != s:
        res[previous[ptr]] = res[ptr] + 2
        ptr = previous[ptr]
        inPath[ptr] = True
    
    for v in range(0, n):
        if inPath[v]:
            res[v] = res[v] // 2 * len(g[v])
            for to in g[v]:
                if not inPath[to]:
                    dfs2(to, v, res[v] // len(g[v]))
    
    res[t] += 1
    
    for i in res:
        print(i % mod, end = ' ')
    print("")
 
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 27)
thread = threading.Thread(target=random_walk)
thread.start()