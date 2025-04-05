# 백준 17142. 연구소 3
# https://www.acmicpc.net/problem/17142

# 가장 처음에 모든 바이러스는 비활성 상태이다.
# 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다.
# 연구소의 바이러스 M개를 활성 상태로 변경하려고 한다.
from collections import deque
def bfs(selected, N, lab):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()

    visited = [[False]* N for _ in range(N)]

    for x, y in selected:
        visited[x][y] = True
        queue.append((x, y, 0))
    
    total_empty = sum(row.count(0) for row in lab)

    time = 0
    infected = 0

    while queue:
        cur_x, cur_y, cur_t = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < N:
                if not visited[next_x][next_y] and lab[next_x][next_y] != 1:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, cur_t + 1))

                    if lab[next_x][next_y] == 0:
                        infected += 1
                        time = max(time, cur_t + 1)
    
    return time if infected == total_empty else float('inf')
                        
def find_min_time(N, M, lab):
    virus_spaces = []

    for i in range(N):
        for j in range(N):
            if lab[i][j] == 2:
                virus_spaces.append((i, j))
    
    min_time = float('inf')

    def dfs(start, selected):
        nonlocal min_time

        if len(selected) == M:
            min_time = min(min_time, bfs(selected, N, lab))
            return
        for i in range(start, len(virus_spaces)):
            selected.append(virus_spaces[i])
            dfs(i + 1, selected)
            selected.pop()
    
    dfs(0, [])

    return min_time if min_time != float('inf') else -1

def main():
    N, M = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(N)]

    print(find_min_time(N, M, lab))

if __name__ == '__main__':
    main()