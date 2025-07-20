def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    result = []

    for i in range(len(arr)):
        count[arr[i]] += 1
    
    for i in range(len(count)):
        for _ in range(count[i]):
            result.append(i)
    
    return result

if __name__ == '__main__':
    arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    print(counting_sort(arr))