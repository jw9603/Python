# https://school.programmers.co.kr/learn/courses/30/lessons/120878
# 유한소수 판별하기

import math
def solution(a, b):
    
    b /= math.gcd(a,b)
    
    for i in [2,5]:
        
        while b % i == 0:
            b //= i
            
    return 1 if b == 1 else 2

if __name__ == '__main__':
    print(solution(7,20))
    print(solution(11,22))
    print(solution(12,21))