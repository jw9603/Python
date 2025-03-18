# 백준 13913. 숨바꼭질 4
# https://www.acmicpc.net/problem/13913
import sys
from collections import deque
def bfs(N, K):
    queue = deque([N])
    visited = [-1] * 100001
    visited[N] = 0
    ways = [-1] * 100001
    
    while queue:
        cur_x = queue.popleft()
        if cur_x == K:
            break

        for next_x in [cur_x - 1, cur_x + 1, 2 * cur_x]:
            if 0 <= next_x <= 100000 and visited[next_x] == -1:
                visited[next_x] = visited[cur_x] + 1
                queue.append((next_x))
                ways[next_x] = cur_x
    return visited[K], ways

def reconstruct(N, K, ways):
    path = []
    curr = K
    while curr != N:
        path.append(curr)
        curr = ways[curr]
    path.append(curr)
    path.reverse()
    return path

def main():
    N, K = map(int, sys.stdin.readline().split())
    time, ways = bfs(N, K)
    paths = reconstruct(N, K, ways)
    print(time)
    print(*paths)

if __name__ == '__main__':
    main()