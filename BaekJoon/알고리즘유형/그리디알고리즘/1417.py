# 백준 1417. 국회의원 선거
# https://www.acmicpc.net/problem/1417
import sys
from heapq import heappop, heappush, heapify
N = int(sys.stdin.readline().strip())
votes = [int(sys.stdin.readline().strip()) for _ in range(N)]
def sol(N, votes):
    dasom = votes[0]
    others = [-v for v in votes[1:]]
    heapify(others)
    cnt = 0
    
    while others and dasom <= others[0]:
        max_votes = -heappop(others)
        dasom += 1
        max_votes -= 1
        cnt += 1
        
        heappush(others, -max_votes)
    return cnt
print(sol(N=N, votes=votes))        
    