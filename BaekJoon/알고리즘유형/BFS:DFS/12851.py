# 백준 12851. 숨바꼭질 2
# https://www.acmicpc.net/problem/12851
import sys
from collections import deque
def bfs(N, K):
    if N == K:
        return 0, 1
    
    visited = [-1] * 100001
    ways = [0] * 100001
    visited[N] = 0
    ways[N] = 1
    queue = deque([(N, 0)])
    
    while queue:
        cur_x, cur_time = queue.popleft()
        
        for next_x in (cur_x -1, cur_x + 1, 2 * cur_x):
            if 0 <= next_x <= 100000:
                if visited[next_x] == -1:
                    visited[next_x] = cur_time + 1
                    ways[next_x] = ways[cur_x]
                    queue.append((next_x, cur_time + 1))
                elif visited[next_x] == cur_time + 1:
                    ways[next_x] += ways[cur_x]
                    
    return visited[K], ways[K]
    

def main():
    N, K = map(int, sys.stdin.readline().split())
    print(*bfs(N=N, K=K), sep='\n')
main()