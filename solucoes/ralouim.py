#!/usr/bin/env python3

# obi2020 - Ralouim
# r. anido
#

N = int(input())
melhor  = [0]*(N+1)
pmelhor = [0]*(N+1)
pdist = [0]*(N+1)


pontos = [[0, 0]]
for i in range(N):
    x,y = [int(i) for i in input().split()]
    pontos.append([x, y])

pares = []
for a in range(N+1):
    for b in range(a+1, N+1):
        dx = pontos[a][0] - pontos[b][0]
        dy = pontos[a][1] - pontos[b][1]
        pares.append([dx * dx + dy * dy, a, b])

pares.sort()
    
for par in pares:
    d = par[0]
    a = par[1]
    b = par[2]

    if d != pdist[a]:
        pdist[a] = d
        pmelhor[a] = melhor[a]
    if d != pdist[b]:
        pdist[b] = d
        pmelhor[b] = melhor[b]

    if a == 0:
        melhor[a] = max(melhor[a], pmelhor[b])
    else:
        melhor[a] = max(melhor[a], 1+pmelhor[b])
        melhor[b] = max(melhor[b], 1+pmelhor[a])    

print(1+melhor[0])
