# 백준 15657. N과 M (8)
# https://www.acmicpc.net/problem/15657
import sys
def combinations(N, M, nums):
    nums.sort()
    ans = []
    def backtrack(start, curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(i, curr)
            curr.pop()
    backtrack(0, [])
    return ans

def main():
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    for perm in combinations(N, M, nums):
        print(*perm)
main()