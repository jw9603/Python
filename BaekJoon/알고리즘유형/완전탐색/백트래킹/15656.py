# 백준 15656. N과 M (7)
# https://www.acmicpc.net/problem/15656
import sys
def permutation(N, M, nums):
    nums.sort()
    ans = []
    def backtrack(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        for num in nums:
            curr.append(num)
            backtrack(curr)
            curr.pop()
    backtrack([])
    return ans

def main():
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    for perm in permutation(N, M, nums):
        print(*perm)
main()