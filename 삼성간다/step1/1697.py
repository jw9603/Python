# 백준 1697. 숨바꼭질
# https://www.acmicpc.net/problem/1697
import sys
from collections import deque
def bfs(N, K):
    queue = deque([(N, 0)])
    visited = [False] * 100001
    while queue:
        cur_x, cur_t = queue.popleft()
        if cur_x == K:
            return cur_t
        for next_x in [cur_x - 1, cur_x + 1, 2 * cur_x]:
            if 0 <= next_x <= 100000 and not visited[next_x]:
                visited[next_x] = True
                queue.append((next_x, cur_t + 1))

def main():
    N, K = map(int, sys.stdin.readline().split())
    print(bfs(N, K))

if __name__ == '__main__':
    main()