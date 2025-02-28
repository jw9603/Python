# 백준 15664. N과 M (10)
# https://www.acmicpc.net/problem/15664
from collections import Counter
import sys
def permutations(N, M, nums):
    nums.sort()
    nums_counts = Counter(nums)
    unique_nums = sorted(nums_counts.keys())
    ans = []
    
    def backtrack(start, curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        
        for i in range(start, len(unique_nums)):
            num = unique_nums[i]
            if curr.count(num) < nums_counts[num]:
                curr.append(num)
                backtrack(i, curr)
                curr.pop()
    backtrack(0, [])
    return ans

def main():
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    for perm in permutations(N=N, M=M, nums=nums):
        print(*perm)
main()

