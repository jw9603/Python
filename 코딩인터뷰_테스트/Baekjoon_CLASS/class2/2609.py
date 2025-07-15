# 백준 2609. 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609
from math import gcd
def gcd(a, b):
    '''
    유클리드 호제법
    gcd(192, 162)
    192 % 162 = 30
    162 % 30 = 12
    30 % 12 = 6
    12 % 6 == 0 -> 끝
    GCD == 6
    즉, a, b = b, a % b
    '''
    while b != 0:
        a, b = b, a % b
    
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def sol(a, b):
    return gcd(a, b), lcm(a, b)

def main():
    a, b = map(int, input().split())
    print(*sol(a, b), sep='\n')

if __name__ == '__main__':
    main()