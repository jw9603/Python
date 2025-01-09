# 백준 2667. 단지번호붙이기
# https://www.acmicpc.net/problem/2667
####################### DFS 풀이 ###########################
import sys
N = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0
home_cnt = []
def dfs(x, y):
    count = 1
    visited[x][y] = True

    for dx, dy in directions:
        next_x = x + dx
        next_y = y + dy
            
        if 0 <= next_x < N and 0 <= next_y < N:
            if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                count += dfs(next_x, next_y)
    return count

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:
            home_cnt.append(dfs(i, j))
            cnt += 1
print(cnt, *sorted(home_cnt),sep='\n')
####################### DFS 풀이 ###########################

####################### BFS 풀이 ###########################
from collections import deque
import sys
N = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0
home_cnt = []
def bfs(x, y):
    count = 1
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))
    
    while queue:
        cur_x, cur_y = queue.popleft()
        for dx, dy in directions:
            next_x = cur_x + dx
            next_y = cur_y + dy
            
            if 0 <= next_x < N and 0 <= next_y < N:
                if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))
                    count += 1
    return count

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:
            home_cnt.append(bfs(i, j))
            cnt += 1
print(cnt, *sorted(home_cnt),sep='\n')
####################### BFS 풀이 ###########################
            
