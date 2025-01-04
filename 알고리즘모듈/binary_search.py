import bisect
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # 값을 찾음
        elif arr[mid] < target:
            left = mid + 1  # 오른쪽으로 이동
        else:
            right = mid - 1  # 왼쪽으로 이동

    return -1  # 값을 찾지 못함

def binary_search_recursive(arr, target, left, right):
    # base case
    if left > right:
        return -1  # 값을 찾지 못함

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid  # 값을 찾음
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


if __name__ == '__main__':
    arr = [1, 3, 2, 4, 5, 8, 7, 11, 23, 31, 10, 9]
    
    arr.sort()
    print(arr)
    
    target = 7
    
    result1 = binary_search(arr, target)
    result2 = binary_search_recursive(arr, target, 0, len(arr) - 1)
    
    print(f"반복문을 사용한 이진 탐색: {result1}")
    print(f"재귀를 사용한 이진 탐색: {result2}")
    
    # Lower Bound
    idx = bisect.bisect_left(arr, 7) # 7이 위치한 인덱스
    print(idx) # 5
    
    # Upper Bound
    idx = bisect.bisect_right(arr, 7)
    print(idx) # 6
    
    # 값 삽입
    bisect.insort(arr, 6)
    print(arr)