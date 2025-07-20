import sys
from collections import deque

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    E = int(data[idx])
    idx += 1
    S = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    
    # Inicializa o grafo como uma lista de adjacência
    grafo = [[] for _ in range(N)]
    for _ in range(M):
        A = int(data[idx])
        idx += 1
        B = int(data[idx])
        idx += 1
        T = int(data[idx])
        idx += 1
        grafo[A].append((B, T))
    
    # Inicializa a matriz de distâncias: dist[rotatória][tempo % 3]
    dist = [[-1 for _ in range(3)] for _ in range(N)]
    queue = deque()
    
    # O ônibus começa na rotatória E no tempo 0
    dist[E][0] = 0
    queue.append((E, 0))
    
    found = False
    answer = -1
    
    while queue:
        current_node, time_mod = queue.popleft()
        current_time = dist[current_node][time_mod]
        
        if current_node == S:
            answer = current_time
            found = True
            break
        
        for (neighbor, T) in grafo[current_node]:
            # Verifica se o semáforo está aberto no tempo atual
            if (T == 1 and time_mod == 0) or (T == 0 and time_mod != 0):
                new_time_mod = (time_mod + 1) % 3
                new_time = current_time + 1
                if dist[neighbor][new_time_mod] == -1 or new_time < dist[neighbor][new_time_mod]:
                    dist[neighbor][new_time_mod] = new_time
                    queue.append((neighbor, new_time_mod))
    
    if found:
        print(answer)
    else:
        print("*")

if __name__ == "__main__":
    main()