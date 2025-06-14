from collections import deque

def bfs(capacity, source, sink, parent):
    n = len(capacity)
    visited = [False] * n
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()
        for v in range(n):
            if not visited[v] and capacity[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

def max_flow(capacity, source, sink):
    n = len(capacity)
    parent = [-1] * n
    max_flow = 0

    while bfs(capacity, source, sink, parent):
        path_flow = float('Inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v])
            v = parent[v]

        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow


capacity = [list(map(int, input().split())) for _ in range(4)]

if len(capacity) != 4 or any(len(row) != 4 for row in capacity):
    print("Error: Invalid input matrix size")
else:
    print("The maximum possible flow is", max_flow(capacity, 0, 3))


# def ford_fulkerson(capacity, source, sink):
#     parent = [-1]*len(capacity)
#     max_flow = 0

#     while bfs(capacity, source, sink, parent):
#         v = sink
#         path_flow = float('inf')
#         while v != source:
#             u = parent[v]
#             path_flow = min(path_flow, capacity[u][v])
#             v = parent[v]

#         v = sink
#         while v!= source:
#             u = parent[v]
#             capacity[u][v] += path_flow
#             capacity[v][u] -= path_flow
#             v = parent[v][u]
        
#         max_flow += path_flow
    
#     return max_flow

# def bfds(capacity, source, sink, parent):
#     n = len(capacity)
#     visited = [False] * n
#     queue = deque()
#     queue.append(source)
#     visited[source] = True

#     while queue:
#         u = queue.popleft()

#         for v in range(n):
#             if not (visited[v] and capacity[u][v] <= 0):
#                 queue.append(v)
#                 visited[v] = True
#                 parent[v] = u
#                 if v == sink:
#                     return True
                
#         return False
