# https://school.programmers.co.kr/learn/courses/30/lessons/181839
# 주사위 게임1
def solution(a, b):
    
    if a % 2 == 1 and b % 2 == 1:
        return a**2 + b**2
    elif a %2 == 1 or b %2 == 1:
        return 2 * (a + b)
    else:
        return abs(a-b)
    
if __name__ == '__main__':
    print(solution(3,5))
    print(solution(6,1))
    print(solution(2,4))