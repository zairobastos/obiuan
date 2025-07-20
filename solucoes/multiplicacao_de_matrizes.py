
import sys

input = sys.stdin.read
data = input().split()

idx = 0
N = int(data[idx])
idx += 1
P = int(data[idx])
idx += 1
Q = int(data[idx])
idx += 1
R = int(data[idx])
idx += 1
S = int(data[idx])
idx += 1
X = int(data[idx])
idx += 1
Y = int(data[idx])
idx += 1
I = int(data[idx])
idx += 1
J = int(data[idx])

total = 0
for k in range(1, N + 1):
    # Calcula A[I][k]
    a = (P * I + Q * k) % X
    # Calcula B[k][J]
    b = (R * k + S * J) % Y
    total += a * b

print(total)

