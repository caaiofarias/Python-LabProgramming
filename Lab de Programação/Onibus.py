def dfs(atual,pai,dist,destino):
    if atual == destino:
        print(dist)
        return True
    for p in g[atual]:
        if p != pai:
            if dfs(p,atual,dist+1,destino):
                return True
    return False
[n,origem,destino] = [int(x) for x in input().split()]
g = [[] for _ in range(n+1)]

for i in range(1,n):
    [P,Q] = [int(x) for x in input().split()]
    g[P].append(Q)
    g[Q].append(P)
dfs(origem,-1,0,destino)

