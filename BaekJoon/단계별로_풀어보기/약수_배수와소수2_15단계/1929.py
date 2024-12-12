# 1929. 소수 구하기
# https://www.acmicpc.net/problem/1929
# 소수란: 1과 자기 자신 외에 나누어지지 않는 양의 정수
import sys
M, N = map(int,sys.stdin.readline().split())

def sol(M, N):
    is_prime = [False] * 2 + [True] * (N - 1)
    
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    return '\n'.join([str(i) for i in range(M, N + 1) if is_prime[i]])

print(sol(M=M, N=N))