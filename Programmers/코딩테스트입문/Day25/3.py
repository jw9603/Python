# https://school.programmers.co.kr/learn/courses/30/lessons/120923
# 연속된 수의 합

def solution(num, total):
    avg = total // num
    return [i for i in range(avg-(num-1)//2,avg+(num+2)//2)]

if __name__ == '__main__':
    print(solution(3,12))
    print(solution(5,15))
    print(solution(4,14))
    print(solution(5,5))