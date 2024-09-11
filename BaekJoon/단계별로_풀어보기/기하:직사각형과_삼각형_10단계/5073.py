# 5073 - 삼각형과 세 변
# https://www.acmicpc.net/problem/5073

import sys

while 1:
    a, b, c = map(int,sys.stdin.readline().split())
    
    if a ==0 and b == 0 and c == 0:
        break
    triangle = [a,b,c]
    triangle.sort()

    if triangle[-1] >= triangle[0] + triangle[1]:
        print('Invalid')  
    elif a == b == c:
        print('Equilateral')
    elif a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')
    
    