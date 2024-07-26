def solution(arr, n):
    for i in range(len(arr)):
        if len(arr) % 2 == 0:
            if i % 2 != 0:
                arr[i] += n
        else:
            if i % 2 == 0:
                arr[i] += n
    return arr

if __name__ == '__main__':
    print(solution([49, 12, 100, 276, 33],27))
    print(solution([444, 555, 666, 777],100))