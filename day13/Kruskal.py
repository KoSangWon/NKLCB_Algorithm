def kruskal(graph):
    def find(node):
        if node != parents[node]:
            parents[node] = find(parents[node]) # path compression
        return parents[node]

    def union(a, b):
        if rank[a] < rank[b]:
            parents[a] = b
        else:
            parents[b] = a
            if rank[a] == rank[b]:
                rank[a] += 1


    parents = [i for i in range(len(graph))]
    rank = [0 for _ in range(len(graph))]

    edges = set()
    for a, adj_list in enumerate(graph):
        for b, w in adj_list:
            if a < b:
                edges.add((w, a, b))
            else:
                edges.add((w, b, a))
    mst = []
    edges = list(edges)
    edges.sort()

    for w, a, b in edges:
        root_a = find(a)
        root_b = find(b)

        if root_a != root_b:
            union(root_a, root_b)
            mst.append((w, a, b))

    return mst


graph = [[(1, 28), (5, 10)], # (인접노드, 가중치)
         [(0, 28), (2, 16), (6, 14)],
         [(1, 16), (3, 12)],
         [(2, 12), (4, 22), (6, 18)],
         [(3, 22), (5, 25), (6, 24)],
         [(0, 10), (4, 25)],
         [(1, 14), (3, 18), (4, 24)]]

print(kruskal(graph))