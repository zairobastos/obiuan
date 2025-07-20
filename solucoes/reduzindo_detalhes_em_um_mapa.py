import sys

input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        self.parent[pu] = pv
        return True

def main():
    N, M = map(int, input().split())
    edges = []

    for _ in range(M):
        u, v, c = map(int, input().split())
        edges.append((c, u - 1, v - 1))

    edges.sort()
    uf = UnionFind(N)
    total = 0

    for cost, u, v in edges:
        if uf.union(u, v):
            total += cost

    print(total)

main()
