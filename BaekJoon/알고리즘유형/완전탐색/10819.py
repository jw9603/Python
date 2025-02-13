# 백준 10819. 차이를 최대로
# https://www.acmicpc.net/problem/10819
######################### 완전 탐색 #########################
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
######################### 완전 탐색 #########################
######################### 백트래킹 ############################
import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))

max_val = 0
used = [False] * N

def calculate(N, arr):
    return sum(abs(arr[i] - arr[i + 1]) for i in range(N - 1))
def permute(A):
    global max_val
    def backtrack(N, curr):
        global max_val
        if len(curr) == len(A):
            max_val = max(max_val, calculate(N, curr))
            return
        
        for i in range(N):
            if not used[i]:
                used[i] = True
                curr.append(A[i])
                backtrack(N, curr)
                curr.pop()
                used[i] = False
    backtrack(N=N, curr=[])
    return max_val
print(permute(A=A))
######################### 백트래킹 ############################
