# 1764. 듣보잡
# https://www.acmicpc.net/problem/1764
import sys

N, M = map(int, sys.stdin.readline().split())
a, b = set(), set()
for _ in range(N):
    a.add(sys.stdin.readline().strip())
for _ in range(M):
    b.add(sys.stdin.readline().strip())   

def sol(a, b):
    result = a & b
    return len(a & b), result

result1, result2 = sol(a=a, b=b)
print(result1)
print('\n'.join(sorted([i for i in result2])))