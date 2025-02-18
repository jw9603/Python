# 백준 13549. 숨바꼭질 3
# https://www.acmicpc.net/problem/13549
import sys
from collections import deque
def bfs(N, K):
    visited = [-1] * 100001
    queue = deque([(N, 0)])
    visited[N] = 0
    
    while queue:
        cur_x, cur_time = queue.popleft()
        
        if cur_x == K:
            return cur_time
        
        if 0<= 2 * cur_x <= 100000 and visited[2 * cur_x] == -1:
            visited[2 * cur_x] = cur_time
            queue.appendleft((2 * cur_x, cur_time))
        
        if 0 <= cur_x - 1 <= 100000 and visited[cur_x - 1] == -1:
            visited[cur_x - 1] = cur_time + 1
            queue.append((cur_x - 1, cur_time + 1))
        
        if 0 <= cur_x + 1 <= 100000 and visited[cur_x + 1] == -1:
            visited[cur_x + 1] = cur_time + 1
            queue.append((cur_x + 1, cur_time + 1))
        

def main():
    N, K = map(int, sys.stdin.readline().split())
    print(bfs(N, K))
main()