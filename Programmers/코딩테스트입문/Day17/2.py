def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n != 0:
            continue
        answer.append(i)
    return answer


##################### 다른 풀이 ##########################
def solution(n,numlist):
    # filter(조건 함수, 순회 가능한 데이터)
    return list(filter(lambda v: v%n == 0, numlist))
##################### 다른 풀이 ##########################

if __name__ == '__main__':
    print(solution(3,[4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(solution(5,[1, 9, 3, 10, 13, 5]))
    print(solution(12,[2, 100, 120, 600, 12, 12]))