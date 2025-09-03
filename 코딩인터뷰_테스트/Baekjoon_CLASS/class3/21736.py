# 백준 21736. 헌내기는 친구가 필요해
# https://www.acmicpc.net/problem/21736
##################################### 문제 이해 #####################################
# 도연이가 있다. 도연이는 비대면 수업 때문에 학교에 가지 못해 아는 친구가 없었다.
# 어서 캠퍼스 내의 사람들과 친해지고 싶다.
# 도연이가 다니는 대학의 캠퍼스는 N * M 크기이며 캠퍼스에서 이동하는 방법은 상하좌우
# 불쌍한 도연이를 위해 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력하는 프로그램

# 입력:
# 첫째 줄에는 캠퍼스의 크기를 나타내는 두 정수 N, M이 주어진다.
# 둘째 줄부터 N개의 줄에는 캠퍼스의 정보들이 주어짐
# 0: 빈 공간, x는 벽, I는 도연이, P는 사람

# 출력:
# 첫째 줄에 도연이가 만날 수 있는 사람의 수를 출력한다. 아무도 만나지 못한 경우 TT를 출력

# 알고리즘:
# 도연이의 위치로부터 P를 볼때마다 += 1 하기, 
# 그렇기 때문에 BFS, DFS 하기
##################################### 문제 이해 #####################################
# BFS 풀이
from collections import deque

def bfs(sx, sy, campus, N, M):
    visited = [[False] * M for _ in range(N)]
    visited[sx][sy] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(sx, sy)])
    cnt = 0
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            
            if not (0 <= next_x < N and 0 <= next_y < M):
                continue
            
            if visited[next_x][next_y]:
                continue
            
            if campus[next_x][next_y] == 'X':
                continue
            
            visited[next_x][next_y] = True
            if campus[next_x][next_y] == 'P':
                cnt += 1
            
            queue.append((next_x, next_y))
    
    return cnt if cnt > 0 else "TT"
                    
def sol(campus, N, M):
    for i in range(N):
        for j in range(M):
            if campus[i][j] == 'I':
                sx, sy = i, j
                break
    
    result = bfs(sx, sy, campus, N, M)
    
    return result
    

def main():
    N, M = map(int, input().split())
    campus = [list(input().strip()) for _ in range(N)]
    
    print(sol(campus, N, M))

if __name__ == '__main__':
    main()
    
# DFS 풀이
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y, campus, N, M, visited):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 0
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        if visited[nx][ny]:
            continue
        if campus[nx][ny] == 'X':
            continue
        
        visited[nx][ny] = True
        if campus[nx][ny] == 'P':
            cnt += 1

        cnt += dfs(nx, ny, campus, N, M, visited)
    return cnt
    
                    
def sol(campus, N, M):
    for i in range(N):
        for j in range(M):
            if campus[i][j] == 'I':
                sx, sy = i, j
                break
            
    visited = [[False] * M for _ in range(N)]
    result = dfs(sx, sy, campus, N, M, visited)
    
    return result if result > 0 else "TT"
    

def main():
    N, M = map(int, input().split())
    campus = [list(input().strip()) for _ in range(N)]
    
    print(sol(campus, N, M))

if __name__ == '__main__':
    main()
    