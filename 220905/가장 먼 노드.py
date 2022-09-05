from collections import deque

def solution(n, vertex):
    graph = [[] for _ in range((n + 1))]

    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    return bfs(graph, 1, n)

def bfs(graph, start, n):
    visited = [0] * (n + 1)
    visited[start] = 1
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = visited[node] + 1
                queue.append(i)

    return visited.count(max(visited))