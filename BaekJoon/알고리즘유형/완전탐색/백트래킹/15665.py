# 백준 15665. N과 M (11)
# https://www.acmicpc.net/problem/15665
import sys

def permutations(N, M, nums):
    nums.sort()
    ans = []
    def backtrack(curr):
        if len(curr) == M:
            ans.append(tuple(curr))
            return
        
        for num in nums:
            curr.append(num)
            backtrack(curr)
            curr.pop()
    backtrack([])
    return sorted(set(ans))

def main():
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    for perm in permutations(N, M, nums):
        print(*perm)
main()