# 백준 17141. 연구소 2
# https://www.acmicpc.net/problem/17141
####################################### itertools #######################################
import sys
from collections import deque
from itertools import combinations
def find_min_time(N, M, lab):
    virus_spaces = []

    for i in range(N):
        for j in range(N):
            if lab[i][j] == 2:
                virus_spaces.append((i, j))

    min_time = float('inf')

    for virus in combinations(virus_spaces, M):
        min_time = min(min_time, bfs(virus, N, lab))
    
    return min_time if min_time != float('inf') else -1

def bfs(virus, N, lab):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    visited = [[False] * N for _ in range(N)]

    for x, y in virus:
        queue.append((x, y, 0))
        visited[x][y] = True

    max_time = 0

    while queue:
        cur_x, cur_y, cur_t = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < N:
                if not visited[next_x][next_y] and lab[next_x][next_y] != 1:
                    queue.append((next_x, next_y, cur_t + 1))
                    visited[next_x][next_y] = True
                    max_time = max(max_time, cur_t + 1)
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and lab[i][j] != 1:
                return float('inf')
    return max_time

def main():
    N, M = map(int, sys.stdin.readline().split())
    lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(find_min_time(N, M, lab))

if __name__ == '__main__':
    main()
####################################### itertools #######################################

####################################### 백트래킹 #######################################
import sys
from collections import deque
def find_min_time(N, M, lab):
    virus_spaces = []

    for i in range(N):
        for j in range(N):
            if lab[i][j] == 2:
                virus_spaces.append((i, j))
    
    min_time = float('inf')

    def backtrack(start, selected):
        nonlocal min_time
        if len(selected) == M:

            min_time = min(min_time, bfs(selected, N, lab))
            return

        for i in range(start, len(virus_spaces)):
            selected.append(virus_spaces[i])
            backtrack(i + 1, selected)
            selected.pop()
    backtrack(0, [])

    return min_time if min_time != float('inf') else -1

def bfs(selected, N, lab):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    visited = [[False] * N for _ in range(N)]

    for x, y in selected:
        queue.append((x, y, 0))
        visited[x][y] = True
    
    max_time = 0

    while queue:
        cur_x, cur_y, cur_t = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < N:
                if not visited[next_x][next_y] and lab[next_x][next_y] != 1:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, cur_t + 1))
                    max_time = max(max_time, cur_t + 1)
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and lab[i][j] != 1:
                return float('inf')
    return max_time

def main():
    N, M = map(int, sys.stdin.readline().split())
    lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(find_min_time(N, M, lab))

if __name__ == '__main__':
    main()
####################################### 백트래킹 #######################################