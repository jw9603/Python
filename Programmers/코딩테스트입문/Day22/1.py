# https://school.programmers.co.kr/learn/courses/30/lessons/120871
# 저주의 숫자 3
def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer

if __name__ == '__main__':
    print(solution(15))
    print(solution(40))