def bubble_sort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swap = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        if not swap:
            break
    
    return arr

def insertion_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        lowest = i
        for j in range(i + 1, len(arr)):
            if arr[lowest] > arr[j]:
                lowest = j
        arr[lowest], arr[i] = arr[i], arr[lowest]
    
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

def merge(left, right):
    left_idx, right_idx = 0, 0
    merged = []

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
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

if __name__ == '__main__':
    a = [1, 3, 2, 6, 5]
    print(bubble_sort(a))
    print(insertion_sort(a))
    print(selection_sort(a))
    print(quick_sort(a))
    print(merge_sort(a))