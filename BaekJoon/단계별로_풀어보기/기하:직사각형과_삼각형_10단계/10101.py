# 10101 - 삼각형 외우기
# https://www.acmicpc.net/problem/10101

import sys

def solution(a,b,c):
    if a == 60 and b == 60 and c == 60:
        return 'Equilateral'
    elif a+b+c == 180:
        if a== b or b == c or c == a:
            return 'Isosceles'
        else:
            return 'Scalene'
    else:
        return 'Error'
            

a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())

print(solution(a,b,c))
