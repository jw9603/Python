# 백준 13913. 숨바꼭질 4
# https://www.acmicpc.net/problem/13913
import sys
from collections import deque
def bfs(N, K):
    visited  = [-1] * 100001
    visited[N] = 0
    queue = deque([(N, 0)])
    prev = [-1] * 100001

    while queue:
        cur_x, cur_time = queue.popleft()
        
        if cur_x == K:
            break
        
        for next_x in [cur_x - 1, cur_x + 1, 2 * cur_x]:
            if 0 <= next_x <= 100000 and visited[next_x] == -1:
                visited[next_x] = cur_time + 1
                queue.append((next_x, cur_time + 1))
                prev[next_x] = cur_x
    return visited[K], prev

def reconstruct_path(N, K, prev):
    cur = K
    path = []
    
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path

def main():
    N, K = map(int, sys.stdin.readline().split())
    time, prev = bfs(N=N, K=K)
    print(time)
    print(*reconstruct_path(N=N, K=K, prev=prev))
main()