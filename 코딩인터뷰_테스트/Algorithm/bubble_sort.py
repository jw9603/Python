def bubble_sort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swap = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        if not swap:
            break
    
    return arr

if __name__ == '__main__':
    arr = [3, 1, 2, 4, 10, 6]

    print(bubble_sort(arr))