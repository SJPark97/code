# 병합 정렬


def merge(left, right):
    merged_arr = []
    i, j = 0, 0  # 왼쪽, 오른쪽 리스트 각각의 인덱스

    while i < len(left) and j < len(right):
        # 왼쪽 리스트의 원소가 작거나 같으면 삽입
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        # 오른쪽 리스트의 원소가 작으면 삽입
        else:
            merged_arr.append(right[j])
            j += 1

    # 왼쪽과 오른쪽 리스트 중 하나라도 원소를 모두 소모하면, 남은 리스트의 원소를 모두 삽입
    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])

    return merged_arr


def merge_sort(arr):
    # 더 이상 분할할 수 없는 경우(종료 조건)
    if len(arr) <= 1:
        return arr

    # 1. 리스트를 분할하여 각각 정렬
    middle = len(arr) // 2
    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])

    # 2. 정렬된 두 리스트를 병합
    return merge(left_arr, right_arr)


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)
