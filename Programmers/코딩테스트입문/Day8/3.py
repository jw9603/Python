def solution(emergency):
    ans = sorted(emergency, reverse=True)
    answer = []
    for i in emergency: 
        answer.append(ans.index(i)+1)
    return answer

if __name__ == '__main__':
    print(solution([3, 76, 24]))
    print(solution([1, 2, 3, 4, 5, 6, 7]))
    print(solution([30, 10, 23, 6, 100]))