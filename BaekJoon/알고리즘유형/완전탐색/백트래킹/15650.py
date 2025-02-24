# 백준 15650. N과 M (2)
# https://www.acmicpc.net/problem/15650
import sys
def combinations(N, M):
    ans = []
    def backtrack(start, curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        
        for i in range(start, N + 1):
            curr.append(i)
            backtrack(i + 1, curr)
            curr.pop()
    backtrack(1, [])
    return ans

def main():
    N, M = map(int, sys.stdin.readline().split())
    for comb in combinations(N=N, M=M):
        print(*comb)
main()
    