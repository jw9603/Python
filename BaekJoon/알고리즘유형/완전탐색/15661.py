# 백준 15661. 링크와 스타트
# https://www.acmicpc.net/problem/15661

############################## 완전 탐색 ############################
import sys
from itertools import combinations
N = int(sys.stdin.readline().strip())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def sol(N, S):
    min_diff = float('inf')
    for k in range(1, (N // 2) + 1):
        for team_start in combinations(range(N), k):
            team_link = [i for i in range(N) if i not in set(team_start)]
            
            ability_start = sum(S[i][j] + S[j][i] for i in team_start for j in team_start if i < j)
            ability_link = sum(S[i][j] + S[j][i] for i in team_link for j in team_link if i < j)
            
            min_diff = min(min_diff, abs(ability_start - ability_link))
            if min_diff == 0:
                print(0)
                sys.exit()
    return min_diff
print(sol(N=N, S=S))
############################## 완전 탐색 ############################

############################## 백트래킹 ############################
import sys
N = int(sys.stdin.readline().strip())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_diff = float('inf')
def backtrack(start, team_start):
    global min_diff
    
    if 1 <= len(team_start) <= N - 1:
        team_link = [i for i in range(N) if i not in set(team_start)]
        
        ability_start = sum(S[i][j] + S[j][i] for i in team_start for j in team_start if i < j)
        ability_link = sum(S[i][j] + S[j][i] for i in team_link for j in team_link if i < j)
        
        min_diff = min(min_diff, abs(ability_start - ability_link))
        if min_diff == 0:
            print(0)
            sys.exit()
        
        
    
    if len(team_start) >= N // 2:
        return
    
    for i in range(start, N):
        team_start.append(i)
        backtrack(i + 1, team_start)
        team_start.pop()
backtrack(0, [])
print(min_diff)
############################## 백트래킹 ############################