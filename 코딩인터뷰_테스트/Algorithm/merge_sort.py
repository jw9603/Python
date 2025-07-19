def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged


def merge_sort(arr):
    # 1. base case
    if len(arr) <= 1:
        return arr
    
    # 2. 재귀 호출
    medium = len(arr) // 2
    left = merge_sort(arr[:medium])
    right = merge_sort(arr[medium:])

    # 3. 데이터 통합
    return merge(left, right)

if __name__ == '__main__':
    arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

    print(merge_sort(arr))