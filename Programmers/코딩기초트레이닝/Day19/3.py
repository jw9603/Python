def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i]:
            answer += [arr[i] for _ in range(arr[i]*2)]
        else:
            answer = answer[:len(answer)-arr[i]]
            
    return answer

if __name__ == '__main__':
    print(solution([3,2,4,1,3],[1, 0, 1, 0, 0]))