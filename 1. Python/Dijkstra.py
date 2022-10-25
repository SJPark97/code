# 1) 일반적인 다익스트라 알고리즘


def dijkstra(start):
    visited = [False] * (n + 1)  # 방문 처리 리스트(최단 거리가 확정된 정점)
    visited[start] = True
    distance[start] = 0

    # 시작 정점과 인접한 정점에 대해 최단 거리 초기화
    for e, w in graph[start]:
        distance[e] = w

    # 시작 정점을 제외한 나머지 정점에 대해서만 반복하므로 n - 1 번 반복함
    for _ in range(n - 1):
        # 1. 최단 거리가 확정되지 않은 정점들 중 최단 거리가 가장 짧은 정점을 선택
        min_dist = INF
        for i in range(1, n + 1):
            if not visited[i] and min_dist > distance[i]:
                min_node = i
                min_dist = distance[i]

        # 2. 해당 정점 최단 거리 확정
        visited[min_node] = True

        # 3. 해당 정점에 인접한 정점에 대해 최단 거리 갱신
        for next_node, dist in graph[min_node]:
            new_dist = distance[min_node] + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist


n, m = map(int, input().split())  # 정점, 간선 개수
graph = [[] for _ in range(n + 1)]
INF = 99999999  # 나올 수 없는 임의의 큰 수
distance = [INF] * (n + 1)  # 출발 정점에서 다른 정점들까지의 최단 거리(무한으로 초기화)

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

dijkstra(1)  # 1번 정점에서 시작
print(distance)

# 2) 힙을 이용한 다익스트라 알고리즘

from heapq import heappush, heappop


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]  # 힙 선언 [(비용, 정점)]

    while heap:
        # 1. 최단 거리가 가장 짧은 정점을 선택
        min_dist, min_node = heappop(heap)

        # 2. 이미 최단 거리로 기록되어 있는 값보다 높은 경우 무시
        if min_dist > distance[min_node]:
            continue

        # 3. 해당 정점에 인접한 정점에 대해 최단 거리 갱신
        for next_node, dist in graph[min_node]:
            new_dist = min_dist + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


n, m = map(int, input().split())  # 정점, 간선 개수
graph = [[] for _ in range(n + 1)]
INF = 99999999  # 나올 수 없는 임의의 큰 수
distance = [INF] * (n + 1)  # 출발 정점에서 다른 정점들까지의 최단 거리(무한으로 초기화)

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

dijkstra(1)  # 1번 정점에서 시작
print(distance)
