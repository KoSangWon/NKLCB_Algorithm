from collections import deque 

class Vertex:
    def __init__(self, value, adj_list=None):
        self.value = value
        if adj_list is None:
            adj_list = []
        self.adj_list = adj_list

class Graph:
    def __init__(self):
        self.vertices = []

    def insert(self, value, adj_list):
        v = Vertex(value, adj_list)
        self.vertices.append(v)
        v_ind = len(self.vertices) - 1

        for adj_v_ind in v.adj_list:
            self.vertices[adj_v_ind].adj_list.append(v_ind)


    def bfs(self, vert_ind, value):
        queue = deque([vert_ind])
        visited = [False] * len(self.vertices) 

        while queue:
            v_ind = queue.popleft()
            v = self.vertices[v_ind]

            if visited[v_ind]:
                continue

            visited[v_ind] = True

            if v.value == value:
                return True

            for adj_v_ind in v.adj_list:
                if visited[adj_v_ind] is False:
                    queue.append(adj_v_ind)

        return False

    def dfs(self, vert_ind, value):
        isFound = False
        visited = [False] * len(self.vertices)
        def recursive(ind):
            nonlocal isFound

            # if visited[ind]:
            #     return

            if isFound:
                return

            visited[ind] = True
            v = self.vertices[ind]
            if v.value == value:
                isFound = True
                return

            for adj_v_ind in v.adj_list:
                if visited[adj_v_ind] is False:
                    recursive(adj_v_ind)
                    
        recursive(vert_ind)
        return isFound

graph = Graph()
graph.insert(0, [])
graph.insert(1, [0])
graph.insert(2, [1])
graph.insert(3, [2])
graph.insert(4, [0, 2, 3])

print(graph.bfs(0, 2))
print(graph.dfs(0, 3))
