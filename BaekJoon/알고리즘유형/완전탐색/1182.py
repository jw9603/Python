# 백준 1182. 부분수열의 합
# https://www.acmicpc.net/problem/1182
import sys
def sol(idx, current_sum):
    global N, S, nums, cnt
    # 1. base case
    if idx == N:
        if current_sum == S:
            cnt += 1
        return
    
    sol(idx + 1, current_sum)
    sol(idx + 1, current_sum + nums[idx])

def main():
    global N, S, nums, cnt
    N, S = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    sol(0, 0)

    print(cnt - 1 if not S else cnt)

if __name__ == '__main__':
    main()
