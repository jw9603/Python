# 백준 15654. N과 M (5)
# https://www.acmicpc.net/problem/15654
import sys
def permutations(M, nums):
    nums.sort()
    ans = []
    def backtrack(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        
        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()
    backtrack([])
    return ans


def main():
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    for perm in permutations(M=M, nums=nums):
        print(*perm)
main()