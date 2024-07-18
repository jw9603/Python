def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i
        if answer > n:
            break
    return answer

if __name__ == '__main__':
    print(solution([34, 5, 71, 29, 100, 34],123))
    print(solution([58, 44, 27, 10, 100],139))