def solve():
    N, K = map(int, input().split())
    
    low = 1
    high = N
    answer = N
    
    while low <= high:
        mid = (low + high) // 2
        total = 0
        term = 1
        valid = False
        
        for i in range(1, K + 1):
            term = term * (mid - i + 1) // i
            total += term
            if total >= N:
                valid = True
                break
        
        if valid:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    
    print(answer)

solve()