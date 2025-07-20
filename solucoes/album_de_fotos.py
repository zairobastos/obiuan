X, Y = map(int, input().split())
L1, H1 = map(int, input().split())
L2, H2 = map(int, input().split())

# Função para verificar se as fotos cabem na página
def cabe(X, Y, L1, H1, L2, H2):
    # Tentar colocar as fotos lado a lado horizontalmente
    if (L1 + L2 <= X) and max(H1, H2) <= Y:
        return True
    # Tentar colocar as fotos lado a lado verticalmente
    if (H1 + H2 <= Y) and max(L1, L2) <= X:
        return True
    # Tentar colocar uma foto horizontal e a outra vertical
    if (L1 + H2 <= X) and max(H1, L2) <= Y:
        return True
    if (H1 + L2 <= X) and max(L1, H2) <= Y:
        return True
    if (L1 + L2 <= Y) and max(H1, H2) <= X:
        return True
    if (H1 + H2 <= X) and max(L1, L2) <= Y:
        return True
    if (L1 + H2 <= Y) and max(H1, L2) <= X:
        return True
    if (H1 + L2 <= Y) and max(L1, H2) <= X:
        return True
    return False

# Verificar todas as combinações possíveis de rotações
if (cabe(X, Y, L1, H1, L2, H2) or
    cabe(X, Y, H1, L1, L2, H2) or
    cabe(X, Y, L1, H1, H2, L2) or
    cabe(X, Y, H1, L1, H2, L2)):
    print("S")
else:
    print("N")