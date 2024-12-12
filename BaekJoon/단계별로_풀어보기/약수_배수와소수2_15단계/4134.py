# 4134. 다음 소수
# https://www.acmicpc.net/problem/4134

import sys
n = int(sys.stdin.readline().strip())

def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    while True:
        if num < 2:
            print(2)
            break
        if is_prime(num):
            print(num)
            break
        else:
            num += 1
            
    
    