# 1) 일반적인 프림 알고리즘


def prim(start):
    visited = [False] * (n + 1)  # MST에 포함 여부 리스트
    distance = [INF] * (n + 1)  # distance[v] => 정점 v가 MST에 속한 정점과 연결된 간선의 비용
    distance[start] = 0
    cost = 0  # MST의 비용 총합(== 최소 비용)

    # 정점의 개수만큼 반복하면서 모든 정점을 이은 MST 생성
    for _ in range(n):
        # 1. MST의 정점에서 이동할 수 있는 모든 정점 중 가장 적은 비용으로 이동 가능한 정점 찾기(Greedy)
        min_dist = INF
        for i, dist in enumerate(distance):
            if not visited[i] and dist < min_dist:
                min_node = i
                min_dist = dist

        # 2. 해당 정점을 MST에 포함하고 비용을 더함
        visited[min_node] = True
        cost += min_dist

        # 3. 해당 정점과 인접한 정점에 대해 최소 비용 갱신
        for next_node, dist in graph[min_node]:
            if not visited[next_node] and dist < distance[next_node]:
                distance[next_node] = dist

    return cost


n, m = map(int, input().split())  # 정점, 간선 개수
graph = [[] for _ in range(n + 1)]
INF = 99999999  # 나올 수 없는 임의의 큰 수

for _ in range(m):
    s, e, w = map(int, input().split())  # 시작 정점, 도착 정점, 비용
    graph[s].append((e, w))
    graph[e].append((s, w))

print(prim(1))  # 1번 정점에서 시작


# 2) 힙을 이용한 프림 알고리즘

from heapq import heappush, heappop


def prim(start):
    visited = [False] * (n + 1)  # MST에 포함 여부 리스트
    heap = [(0, start)]  # 힙 선언 [(비용, 정점)]
    cost = 0  # MST의 가중치 총합(== 최소 비용)

    while heap:
        # 1. 가장 적은 비용으로 이동 가능한 정점 찾기(Greedy)
        min_dist, min_node = heappop(heap)  # 최소힙이므로 튜플의 첫 번째 원소를 기준으로 최소값 pop
        if visited[min_node]:
            continue  # 이미 MST에 포함된 정점이라면 무시

        # 2. 해당 정점을 MST에 포함하고 비용 총합을 더함
        visited[min_node] = True
        cost += min_dist

        # 3. 해당 정점과 인접한 정점에 대해 heappush
        for next_node, dist in graph[min_node]:
            if not visited[next_node]:
                heappush(heap, (dist, next_node))

    return cost


n, m = map(int, input().split())  # 정점, 간선 개수
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())  # 시작 정점, 도착 정점, 비용
    graph[s].append((e, w))
    graph[e].append((s, w))

print(prim(1))  # 1번 정점에서 시작
