# 백준 13549. 숨바꼭질 3
# https://www.acmicpc.net/problem/13549
import sys
from collections import deque
def bfs(N, K):
    queue = deque([(N, 0)])
    visited = [False] * 100001
    visited[N] = True

    while queue:
        cur_x, cur_t = queue.popleft()

        if cur_x == K:
            return cur_t
        
        if 0 <= cur_x * 2 <= 100000 and not visited[cur_x * 2]:
            visited[2 * cur_x] = True
            queue.append((cur_x * 2, cur_t))
        
        if 0 <= cur_x - 1 <= 100000 and not visited[cur_x - 1]:
            visited[cur_x - 1] = True
            queue.append((cur_x - 1, cur_t + 1))

        if 0 <= cur_x + 1 <= 100000 and not visited[cur_x + 1]:
            visited[cur_x + 1] = True
            queue.append((cur_x + 1, cur_t + 1))

def main():
    N, K = map(int, sys.stdin.readline().split())
    print(bfs(N, K))

if __name__ == '__main__':
    main()