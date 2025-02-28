# 백준 15666. N과 M (12)
# https://www.acmicpc.net/problem/15666
import sys
def combinations(N, M, nums):
    nums.sort()
    ans = []
    def backtrack(start, curr):
        if len(curr) == M:
            ans.append(tuple(curr))
            return
        
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(i, curr)
            curr.pop()
    backtrack(0, [])
    return sorted(set(ans))

def main():
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    for comb in combinations(N, M, nums):
        print(*comb)
main()  
