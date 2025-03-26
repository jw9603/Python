# 최대공약수와 최소공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/12940
from math import gcd
def lcm(n, m):
    return n * m // gcd(n ,m)

def solution(n, m):
    return [gcd(n, m), lcm(n, m)]

if __name__ == '__main__':
    n1, m1 = 3, 12
    n2, m2 = 2, 5
    print(f"Result1: {solution(n=n1, m=m1)}")
    print(f"Result2: {solution(n=n2, m=m2)}")