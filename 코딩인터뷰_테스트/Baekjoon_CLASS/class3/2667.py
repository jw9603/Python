# 백준 2667. 단지번호붙이기
# https://www.acmicpc.net/problem/2667
##################################### 문제 이해 #####################################
# 1: 집이 있는 곳, 0: 집이 없는곳
# 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 연결되었다는 것은 상하좌우로 연결된 경우!

# 입력:
# 첫 번째 줄에는 지도의 크기 N,

# 출력:
# 첫 번째 줄에는 총 단지 수를 출력, 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력

# 알고리즘:
# 지도를 순회하면서 1이 나오면 이때부터 BFS or DFS를 수행!

##################################### 문제 이해 #####################################
# BFS
# from collections import deque
# def bfs(x, y, grid, visited, N):
#     visited[x][y] = True
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     queue = deque([(x, y)])
#     home_cnt = 1

#     while queue:
#         cur_x, cur_y = queue.popleft()
        
#         for dx, dy in directions:
#             next_x = cur_x + dx
#             next_y = cur_y + dy
#             if 0 <= next_x < N and 0 <= next_y < N:
#                 if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
#                     visited[next_x][next_y] = True
#                     queue.append((next_x, next_y))
#                     home_cnt += 1
    
#     return home_cnt

# def sol(grid, N):
#     cnt = 0
#     cnt_list = []
#     visited = [[False] * N for _ in range(N)]

#     for i in range(N):
#         for j in range(N):
#             if grid[i][j] == 1 and not visited[i][j]:
#                 cnt_list.append(bfs(i, j, grid, visited, N))
#                 cnt += 1
    
#     return cnt, *sorted(cnt_list)


# def main():
#     N = int(input().strip())
#     grid = [list(map(int, input().strip())) for _ in range(N)]

#     print(*sol(grid, N), sep='\n')

# if __name__ == '__main__':
#     main()

# DFS
def dfs(x, y, grid, visited, N, home_cnt):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    home_cnt = 1
    
    for dx, dy in directions:
        next_x = x + dx
        next_y = y + dy
        if 0 <= next_x < N and 0 <= next_y < N:
            if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                home_cnt += dfs(next_x, next_y, grid, visited, N, home_cnt)
    
    return home_cnt

def sol(grid, N):
    cnt = 0
    cnt_list = []
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1 and not visited[i][j]:
                cnt_list.append(dfs(i, j, grid, visited, N, 1))
                cnt += 1
    
    return cnt, *sorted(cnt_list)


def main():
    N = int(input().strip())
    grid = [list(map(int, input().strip())) for _ in range(N)]

    print(*sol(grid, N), sep='\n')

if __name__ == '__main__':
    main()