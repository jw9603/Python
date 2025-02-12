# 백준 1182. 부분수열의 합
# https://www.acmicpc.net/problem/1182
import sys
N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

cnt = 0
def sol(search_idx, current_sum):
    global cnt
    
    if search_idx == N:
        if current_sum == S:
            cnt += 1
        return
    
    sol(search_idx + 1, current_sum)
    sol(search_idx + 1, current_sum + nums[search_idx])

sol(0, 0)
if S == 0:
    cnt -= 1
print(cnt)