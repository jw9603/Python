# 백준 15649. N과 M (1)
# https://www.acmicpc.net/problem/15649
import sys
def permutation(N, M):
    ans = []
    def backtrack(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        for i in range(1, N + 1):
            if i not in curr:
                curr.append(i)
                backtrack(curr)
                curr.pop()
    backtrack([])
    return ans 


def main():
    N, M = map(int, sys.stdin.readline().split())
    for perm in permutation(N=N, M=M):
        print(*perm)
        
main()
    