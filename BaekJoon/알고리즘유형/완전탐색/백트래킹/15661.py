# 백준 15661. 링크와 스타트
# https://www.acmicpc.net/problem/15661
#################################### itertools ####################################
import sys
from itertools import combinations
def check_min_diff(N, S):
    min_diff = float('inf')
    for k in range(1, (N // 2) + 1):
        for team_start in combinations(range(N), k):
            team_link = [i for i in range(N) if i not in set(team_start)]

            ability_start = sum(S[i][j] + S[j][i] for i in team_start for j in team_start if i < j)
            ability_link = sum(S[i][j] + S[j][i] for i in team_link for j in team_link if i < j)

            min_diff = min(min_diff, abs(ability_start - ability_link))
            if min_diff == 0:
                return 0
    return min_diff
                

def main():
    N = int(sys.stdin.readline().strip())
    S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(check_min_diff(N, S))

if __name__ == '__main__':
    main()
#################################### itertools ####################################

#################################### 백트래킹 ####################################
import sys

def backtrack(start, team_start):
    global min_diff, N, S
    if 1 <= len(team_start) <= N - 1:
        team_link = [i for i in range(N) if i not in set(team_start)]

        ability_start = sum(S[i][j] + S[j][i] for i in team_start for j in team_start if i < j)
        ability_link = sum(S[i][j] + S[j][i] for i in team_link for j in team_link if i < j)

        min_diff = min(min_diff, abs(ability_start - ability_link))

        if min_diff == 0:
            return
    
    if len(team_start) >= N // 2:
        return
    
    for i in range(start, N):
        team_start.append(i)
        backtrack(i + 1, team_start)
        team_start.pop()

def main():
    global min_diff, N, S
    N = int(sys.stdin.readline().strip())
    S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    min_diff = float('inf')

    backtrack(0, [])

    print(min_diff)

if __name__ == '__main__':
    main()
#################################### 백트래킹 ####################################