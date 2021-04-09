import heapq

def dijkstra(start, graph):
    n = len(graph)
    heap = []
    distances = [float('inf')] * n

    heapq.heappush(heap, (0, start))
    distances[start] = 0

    while heap:
        dist, node = heapq.heappop(heap)

        if dist > distances[node]:
            continue

        for adj_node, adj_dist in graph[node]:
            new_dist = dist + adj_dist
            if new_dist < distances[adj_node]:
                distances[adj_node] = new_dist
                heapq.heappush(heap, (new_dist, adj_node))
    
    return distances