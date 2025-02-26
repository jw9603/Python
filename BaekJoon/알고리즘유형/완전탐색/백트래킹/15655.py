# 백준 15655. N과 M (6)
# https://www.acmicpc.net/problem/15655
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
            backtrack(i + 1, curr)
            curr.pop()
    backtrack(0, [])
    return ans
            
def main():
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    for comb in combinations(N=N, M=M, nums=nums):
        print(*comb)
main()