import sys
MOD = 10**9 + 7

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    K = int(data[idx])
    idx += 1
    H = []
    for _ in range(1 << N):
        H.append(int(data[idx]))
        idx += 1
    
    h_juquinha = H[0]
    S = sorted(H)
    rank = S.index(h_juquinha)
    m = (1 << N) - 1 - rank
    
    if K == N + 1:
        total = 1
        for i in range(N):
            total = total * (rank - i) % MOD
        print(total)
        return
    
    if m < (1 << (N - K + 1)) - 1:
        print(0)
        return
    
    a = 1
    for i in range(K - 1):
        a = a * (rank - i) % MOD
    
    b = 1
    for i in range(1 << (N - K)):
        b = b * (m - i) % MOD
    
    c = 1
    for i in range(1, 1 << (N - K + 1)):
        c = c * i % MOD
    
    total = a * b % MOD
    total = total * pow(c, MOD - 2, MOD) % MOD
    total = total * (1 << (N - K + 1)) % MOD
    print(total)

if __name__ == "__main__":
    main()