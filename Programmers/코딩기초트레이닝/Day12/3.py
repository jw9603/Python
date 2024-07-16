def solution(arr, intervals):
    answer = []
    for i in intervals:
        answer+=arr[i[0]:i[1]+1]
    return answer

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5],[[1, 3], [0, 4]]))