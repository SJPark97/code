# 힙 모듈 사용
# 파이썬은 기본적으로 최소힙!

from heapq import heappush, heappop

heap = []

# 최소
heappush(heap, 2)
heappush(heap, 5)
heappush(heap, 7)
heappush(heap, 3)
heappush(heap, 4)
heappush(heap, 6)
print(heap)

while heap:
    print(heappop(heap))
# 최대
heappush(heap, (-2, 2))
heappush(heap, (-5, 5))
heappush(heap, (-7, 7))
heappush(heap, (-3, 3))
heappush(heap, (-4, 4))
heappush(heap, (-6, 6))

while heap:
    print(heappop(heap)[1])


# 최소힙 구현

# 힙 삽입 연산
def heap_push(item):
    heap.append(item)
    child = len(heap) - 1
    parent = child // 2

    # 루트 노드이거나 최소힙 조건을 만족하지 못하면 종료
    while parent > 0 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2


# 힙 삭제 연산
def heap_pop():
    # 루트 노드만 남은 경우 바로 반환
    if len(heap) <= 2:
        return heap.pop()

    item = heap[1]  # 루트 노드 백업
    heap[1] = heap.pop()  # 마지막 노드를 루트 노드로 이동
    parent = 1
    child = parent * 2

    while child < len(heap):  # 자식이 하나라도 있으면
        if child + 1 < len(heap) and heap[child] > heap[child + 1]:
            # 오른쪽 자식이 있고, 오른쪽 자식이 왼쪽 자식보다 작다면
            child += 1  # 비교 대상을 오른쪽 자식으로 갱신

        # 자식이 더 작으면 최소힙이 아니므로 노드 교환
        if heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
            child = parent * 2
        # 최소힙 만족하면 탈출
        else:
            break

    return item  # 백업했던 루트 노드 반환


heap = [0]
heap_push(2)
heap_push(5)
heap_push(7)
heap_push(3)
heap_push(4)
heap_push(6)
print(heap)

while len(heap) >= 2:
    print(heap_pop())

# 최대힙 구현

# 힙 삽입 연산
def heap_push(item):
    heap.append(item)
    child = len(heap) - 1
    parent = child // 2

    # 루트 노드이거나 최대힙 조건을 만족하지 못하면 종료
    while parent > 0 and heap[parent] < heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2


# 힙 삭제 연산
def heap_pop():
    # 루트 노드만 남은 경우 바로 반환
    if len(heap) <= 2:
        return heap.pop()

    item = heap[1]  # 루트 노드 백업
    heap[1] = heap.pop()  # 마지막 노드를 루트 노드로 이동
    parent = 1
    child = parent * 2

    while child < len(heap):  # 자식이 하나라도 있으면
        if child + 1 < len(heap) and heap[child] < heap[child + 1]:
            # 오른쪽 자식이 있고, 오른쪽 자식이 왼쪽 자식보다 크다면
            child += 1  # 비교 대상을 오른쪽 자식으로 갱신

        # 자식이 더 크면 최대힙이 아니므로 노드 교환
        if heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
            child = parent * 2
        # 최대힙 만족하면 탈출
        else:
            break

    return item  # 백업했던 루트 노드 반환


heap = [0]
heap_push(2)
heap_push(5)
heap_push(7)
heap_push(3)
heap_push(4)
heap_push(6)
print(heap)

while len(heap) >= 2:
    print(heap_pop())
