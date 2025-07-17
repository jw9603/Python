def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

    return arr

if __name__ == '__main__':
    arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

    print(insertion_sort(arr))