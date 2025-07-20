C, N = map(int, input().split())
clientes = [tuple(map(int, input().split())) for _ in range(N)]

caixas = [0] * C
atrasados = 0

for T, D in clientes:
    idx = caixas.index(min(caixas))
    inicio = max(caixas[idx], T)
    if inicio - T > 20:
        atrasados += 1
    caixas[idx] = inicio + D

print(atrasados)
