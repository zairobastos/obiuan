import sys
sys.setrecursionlimit(10000)
from functools import lru_cache

MOD = 10007

# Função principal
def main():
    N = int(input())
    peças = input().split()

    # Converter para máscara binária (bitmask): 1 = P, 0 = B
    estado_inicial = 0
    for i in range(N):
        if peças[i] == 'P':
            estado_inicial |= (1 << i)

    @lru_cache(maxsize=None)
    def conta_solucoes(estado, n):
        if estado == 0:
            return 1  # sucesso: todas as peças removidas
        
        total = 0
        for i in range(n):
            if (estado >> i) & 1 == 1:  # só pode remover peças pretas
                novo_estado = estado & ~(1 << i)  # remove a peça i

                # inverter vizinhos
                for vizinho in [i-1, i+1]:
                    if 0 <= vizinho < n:
                        novo_estado ^= (1 << vizinho)  # inverte vizinho

                total += conta_solucoes(novo_estado, n)
                total %= MOD
        
        return total

    print(conta_solucoes(estado_inicial, N))

main()
