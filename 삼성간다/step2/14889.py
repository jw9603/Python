# 백준 14889. 스타트와 링크
# https://www.acmicpc.net/problem/14889
################################### 백트래킹 ###################################
def dfs(start, team_start):
    global N, S, min_diff

    if len(team_start) == N // 2:
        team_link = [i for i in range(N) if i not in team_start]

        ability_start = sum(S[i][j] + S[j][i] for i in team_start for j in team_start if i < j)
        ability_link = sum(S[i][j] + S[j][i] for i in team_link for j in team_link if i < j)

        min_diff = min(min_diff, abs(ability_start - ability_link))
        return
    
    for i in range(start, N):
        team_start.append(i)
        dfs(i + 1, team_start)
        team_start.pop()

def main():
    global N, S, min_diff
    N = int(input().strip())
    S = [list(map(int, input().split())) for _ in range(N)]
    min_diff = float('inf')

    dfs(0, [])

    print(min_diff)

if __name__ == '__main__':
    main()
################################### 백트래킹 ###################################

################################### itertools ###################################
from itertools import combinations
def sol(N, S):
    min_diff = float('inf')

    for team_start in combinations(range(N), N // 2):
        team_link = [i for i in range(N) if i not in set(team_start)]

        ability_start = sum(S[i][j] + S[j][i] for i in team_start for j in team_start if i < j)
        ability_link = sum(S[i][j] + S[j][i] for i in team_link for j in team_link if i < j)

        min_diff = min(min_diff, abs(ability_start - ability_link))
    
    return min_diff
    
def main():
    N = int(input().strip())
    S = [list(map(int, input().split())) for _ in range(N)]

    print(sol(N, S))

if __name__ == '__main__':
    main()
################################### itertools ###################################