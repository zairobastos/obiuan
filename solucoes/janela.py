F1, F2, F3 = map(int, input().split())
folhas = sorted([F1, F2, F3])

area_aberta = 0

area_aberta += max(0, folhas[0] - 0) * 100

for i in range(1, 3):
    inicio = folhas[i-1] + 200
    fim = folhas[i]
    if inicio < fim:
        area_aberta += (fim - inicio) * 100

area_aberta += max(0, 600 - (folhas[2] + 200)) * 100

print(area_aberta)