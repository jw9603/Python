# 백준 15663. N과 M (9)
# https://www.acmicpc.net/problem/15663
import sys
from collections import Counter
def permutations(N, M, nums):
    nums.sort()
    ans = []
    def backtrack(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        
        num_counts = Counter(nums)
        for num in num_counts:
            if curr.count(num) < num_counts[num]:
                curr.append(num)
                backtrack(curr)
                curr.pop()
    backtrack([])
    return ans

def main():
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    for perm in permutations(N, M, nums):
        print(*perm)
main()