# 백준 2667. 단지번호붙이기
# https://www.acmicpc.net/problem/2667

################################### BFS 풀이 ###################################
import sys
from collections import deque
def bfs(x, y, N, visited):
    visited[x][y] = True
    queue = deque([(x, y)])
    home_cnt = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < N and 0 <= next_y < N:
                if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))
                    home_cnt += 1
    return home_cnt
    
def main():
    global grid
    N = int(sys.stdin.readline().strip())
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    cnts = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1 and not visited[i][j]:
                cnts.append(bfs(i, j, N, visited))
    print(len(cnts), *sorted(cnts), sep='\n')

if __name__ == '__main__':
    main()
################################### BFS 풀이 ###################################

################################### DFS 풀이 ###################################
import sys
def dfs(x, y, N, visited):
    visited[x][y] = True
    home_cnt = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < N and 0 <= next_y < N:
            if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                home_cnt += dfs(next_x, next_y, N, visited)
    return home_cnt
    
def main():
    global grid
    N = int(sys.stdin.readline().strip())
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    cnts = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1 and not visited[i][j]:
                cnts.append(dfs(i, j, N, visited))
    print(len(cnts), *sorted(cnts), sep='\n')

if __name__ == '__main__':
    main()
################################### DFS 풀이 ###################################