def solution(box, n):
    answer = 1
    for i in box:
        answer *= i // n
    return answer

if __name__ == '__main__':
    print(solution([1,1,1],1))
    print(solution([10,8,6],3))