A = int(input())
N = int(input())

visiveis = 0
for _ in range(N):
    F = int(input())
    if A * F >= 40000000:
        visiveis += 1

print(visiveis)
