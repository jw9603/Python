# 백준 2178. 미로 탐색
# https://www.acmicpc.net/problem/2178
############################## 문제 이해 ##############################
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램
# 을 작성해라. 서로 인접한 칸으로만 이동할 수 있다.
# 칸을 셀 때에는 시작 위치와 도착 위치도 포함된다.
# 입력:
# 첫째 줄에 두 정수 N, M이 주어진다.
# 출력:
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다.
# 알고리즘:
# 도착지점까지 이동하는 최소의 칸 수를 구하는 문제이므로 BFS를 사용한다.
############################## 문제 이해 ##############################
from collections import deque
def bfs(graph, n, m):
    queue = deque([(0, 0, 1)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    
    while queue:
        cur_x, cur_y, cur_d = queue.popleft()
        
        if cur_x == n - 1 and cur_y == m - 1:
            return cur_d
        
        for dx, dy in directions:
            nx, ny = cur_x + dx, cur_y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cur_d + 1))
                
def main():
    n, m = map(int, input().split())
    graph = [list(map(int, input().strip())) for _ in range(n)]
    print(bfs(graph, n, m))

if __name__ == "__main__":
    main()