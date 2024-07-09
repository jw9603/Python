def solution(arr, queries):
    for i in range(len(queries)):
        arr[queries[i][0]], arr[queries[i][1]] = arr[queries[i][1]], arr[queries[i][0]]
    return arr

if __name__ =='__main__':
    print([0, 1, 2, 3, 4],[[0, 3],[1, 2],[1, 4]])