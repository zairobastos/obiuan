# Leitura da entrada
N = int(input())
casas = [int(input()) for _ in range(N)]
K = int(input())

# Inicializando ponteiros
i = 0
j = N - 1

# Usando dois ponteiros para encontrar o par único cuja soma é K
while i < j:
    soma = casas[i] + casas[j]
    if soma == K:
        print(casas[i], casas[j])
        break
    elif soma < K:
        i += 1
    else:
        j -= 1
