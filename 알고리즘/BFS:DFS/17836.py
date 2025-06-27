# 백준 17836. 공주님을 구해라!
# https://www.acmicpc.net/problem/17836
######################################### 문제 이해 #########################################
# (N, M) 크기의 성 입구 (1, 1)으로 들어왔다 -> 1-index
# 마왕은 용사가 공주를 찾지 못하도록 성의 여러 군데 마법 벽을 세워놓았다.
# 용사는 현재의 가지고 있는 무기로는 마법 벽을 통과할 수 없으며, 마법 벽을 피해 (N, M) 위치에 있는 공주님을 구출해야 한다.
# 마왕은 용사를 괴롭히기 위해 공주에게 저주를 걸었다.
# 저주에 걸린 공주는 T시간 이내로 용사를 만나지 못한다면 영원히 돌로 변하게 된다.
# 반드시 T시간 이내에 도달해야 한다. 용사는 한 칸을 이동하는 데 한 시간이 걸린다.
# 용사는 상하좌우 이동 가능, 명검 그람이 숨겨져 있다.
# 그람을 구하면 마법의 벽이 있는 칸일지라도, 단숨에 벽을 부수고 그 공간으로 갈 수 있다.

# 입력
# 성의 크기인 N, M, T가 주어진다.
# 0은 빈 공간, 1은 마법의 벽, 2는 그람, (1, 1)과 (N, M)은 0이다.

# 출력: 용사가 T시간 이내에 공주에게 도달할 수 있다면, 그 최단 시간 출력
# 없다면 'Fail'을 출력

# 알고리즘
# BFS를 사용
######################################### 문제 이해 #########################################
from collections import deque
def bfs(N, M, T, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    queue = deque([(0, 0, 0)])
    min_time, gram_time = float('inf'), float('inf')

    while queue:
        cur_x, cur_y, cur_t = queue.popleft()

        if cur_t > T:
            continue

        if cur_x == N - 1 and cur_y == M - 1:
            min_time = min(min_time, cur_t)
        
        if grid[cur_x][cur_y] == 2:
            gram_time = cur_t + (N - 1 - cur_x) + (M - 1 - cur_y)
        
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y]:
                if grid[next_x][next_y] != 1:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, cur_t + 1))

    time = min(min_time, gram_time)

    return time if time <= T else "Fail"

def main():
    N, M, T = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    print(bfs(N, M, T, grid))

if __name__ == '__main__':
    main()