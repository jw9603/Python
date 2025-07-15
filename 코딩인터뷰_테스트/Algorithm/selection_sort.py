def selection_sort(arr):
    for i in range(len(arr)):
        lowest = i
        for j in range(i + 1, len(arr)):
            if arr[lowest] > arr[j]:
                lowest = j
        arr[lowest], arr[i] = arr[i], arr[lowest]
    
    return arr

if __name__ == '__main__':
    arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

    print(selection_sort(arr))