# https://school.programmers.co.kr/learn/courses/30/lessons/120884
# 치킨 쿠폰
def solution(chicken):
    answer = 0
    while chicken >= 10:
        answer += chicken // 10
        chicken = chicken // 10 + chicken % 10
    return answer

if __name__ == '__main__':
    print(solution(100))
    print(solution(1081))