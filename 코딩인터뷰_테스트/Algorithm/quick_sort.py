def quick_sort_in_place(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    quick_sort_in_place(arr, start, right - 1)
    quick_sort_in_place(arr, right + 1, end)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x < pivot]
    right = [x for x in tail if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

    quick_sort_in_place(arr, 0, len(arr) - 1)
    print(f"Quick Sort In-Place 방식: {arr}")

    arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    print(f"Quick Sort: {quick_sort(arr)}")