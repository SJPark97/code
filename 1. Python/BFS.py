def bfs(v):
    visited[v] = True
    queue = [v]
    print(v, end=' ')

    while queue:
        v = queue.pop(0)
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)
                print(next_v, end=' ')


n, m = map(int, input().split())

edges = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(0, len(edges), 2):
    v1, v2 = edges[i], edges[i + 1]
    graph[v1].append(v2)
    graph[v2].append(v1)

bfs(1)
