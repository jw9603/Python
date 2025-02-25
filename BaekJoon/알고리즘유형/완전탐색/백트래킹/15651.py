# 백준 15651. N과 M (3)
# https://www.acmicpc.net/problem/15651
import sys
def duplicated_permutation(N, M):
    ans = []
    def backtrack(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        
        for i in range(1, N + 1):
            curr.append(i)
            backtrack(curr)
            curr.pop()
    backtrack([])
    return ans

def main():
    N, M = map(int, sys.stdin.readline().split())
    
    for dp in duplicated_permutation(N=N, M=M):
        print(*dp)
main()
    