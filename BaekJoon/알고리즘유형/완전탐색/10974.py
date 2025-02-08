# 백준 10974. 모든 순열
# https://www.acmicpc.net/problem/10974
import sys
N = int(sys.stdin.readline().strip())
def permutation(N):
    nums = [i for i in range(1, N + 1)]
    ans = []
    def backtrack(curr):
        if len(curr) == N:
            ans.append(curr[:])
            return
        
        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()
    backtrack([])
    return ans
result = permutation(N=N)
for perm in result:
    print(*perm)