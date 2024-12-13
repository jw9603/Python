# 4948. 베르트랑 공준
# https://www.acmicpc.net/problem/4948

import sys

def sol(n, m):
    '''
    n보다 크고, 2n(==m)보다 작거나 같은 소수의 개수를 출력하는 함수
    '''
    is_prime = [False] * 2 + [True] * (m - 1)
    
    for i in range(2, int(m ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, m + 1, i):
                is_prime[j] = False
    return len([i for i in range(n + 1, m + 1) if is_prime[i]])

while True:
    num = int(sys.stdin.readline().strip())
    if num == 0:
        break
    print(sol(n=num, m= 2 * num))
    