import sys
import heapq

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    in_degree = [0] * N

    for _ in range(M):
        A, B = map(int, input().split())
        adj[A].append(B)
        in_degree[B] += 1

    # heapq em Python é min-heap, o que é ótimo pois queremos prioridades menores (índices menores)
    heap = []
    for i in range(N):
        if in_degree[i] == 0:
            heapq.heappush(heap, i)

    ordem = []
    while heap:
        u = heapq.heappop(heap)
        ordem.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(heap, v)

    if len(ordem) != N:
        print("*")
    else:
        for t in ordem:
            print(t)

main()
