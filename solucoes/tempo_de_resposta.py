def main():
    N = int(input())
    registros = [input().split() for _ in range(N)]

    tempo_atual = 0
    tempo_total = {}  # amigo -> tempo total de resposta
    aguardando_resposta = {}  # amigo -> tempo da última mensagem recebida ainda não respondida
    amigos = set()

    for reg in registros:
        tipo, x = reg[0], int(reg[1])

        if tipo == 'T':
            tempo_atual += x
        elif tipo == 'R':
            amigos.add(x)
            aguardando_resposta[x] = tempo_atual
        elif tipo == 'E':
            amigos.add(x)
            if x in aguardando_resposta:
                inicio = aguardando_resposta.pop(x)
                tempo_total[x] = tempo_total.get(x, 0) + (tempo_atual - inicio)
            else:
                # Caso inesperado, mas seguindo a descrição, isso não deve acontecer
                tempo_total[x] = -1

        # Se não for um T, e nenhum tempo foi incrementado, conta como 1 segundo
        if tipo != 'T':
            tempo_atual += 1

    # Gerar saída em ordem crescente dos amigos
    for amigo in sorted(amigos):
        if amigo in aguardando_resposta:
            print(amigo, -1)
        else:
            print(amigo, tempo_total.get(amigo, 0))

main()
