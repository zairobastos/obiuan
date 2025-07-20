def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1

    parent = list(range(N + 1))  # parent[i] = pai de i (de 1 a N)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x  # Une os conjuntos

    while idx < len(data):
        a = int(data[idx])
        b = int(data[idx + 1])
        union(a, b)
        idx += 2

    # Contar quantas raízes únicas existem
    familias = set()
    for i in range(1, N + 1):
        familias.add(find(i))

    print(len(familias))

main()
