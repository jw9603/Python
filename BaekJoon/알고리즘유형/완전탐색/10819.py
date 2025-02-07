# 백준 10819. 차이를 최대로
# https://www.acmicpc.net/problem/10819
import sys
from itertools import permutations
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
def sol(N, A):
    max_val = 0
    for perm in permutations(A):
        current_val = 0
        for i in range(N - 1):
            current_val += abs(perm[i] - perm[i + 1])
        max_val = max(max_val, current_val)
    return max_val
print(sol(N=N, A=A))