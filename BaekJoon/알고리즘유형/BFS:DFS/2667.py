# 백준 2667. 단지번호붙이기
# https://www.acmicpc.net/problem/2667
################################ BFS 풀이 ###################################
import sys
from collections import deque
                
def main():
    N = int(sys.stdin.readline().strip())
    visited = [[False] * N for _ in range(N)]
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    cnt = 0
    def bfs(x, y):
        home_cnt = 1
        visited[x][y] = True
        q = deque()
        q.append((x, y))
        directions = [(-1, 0), (1, 0),(0, -1), (0, 1)]
        while q:
            cur_x, cur_y = q.popleft()
            for dx, dy in directions:
                next_x = cur_x + dx
                next_y = cur_y + dy
                if 0 <= next_x and next_x < N and 0 <= next_y and next_y < N:
                    if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y))
                        home_cnt += 1
        return home_cnt
    result = []             
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1 and not visited[i][j]:
                result.append(bfs(i, j))
                cnt += 1
    print(cnt, *sorted(result),sep='\n')
main()
################################ BFS 풀이 ###################################

################################ DFS 풀이 ###################################
import sys
def main():
    N = int(sys.stdin.readline().strip())
    visited = [[False] * N for _ in range(N)]
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    cnt = 0
    def dfs(x, y, home_cnt):
        home_cnt = 1
        visited[x][y] = True
        directions = [(-1, 0), (1, 0),(0, -1), (0, 1)]
    
        for dx, dy in directions:
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x and next_x < N and 0 <= next_y and next_y < N:
                if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    home_cnt += dfs(next_x, next_y, home_cnt)
        return home_cnt
    result = []             
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1 and not visited[i][j]:
                result.append(dfs(i, j, 1))
                cnt += 1
    print(cnt, *sorted(result),sep='\n')
main()
################################ DFS 풀이 ###################################
            