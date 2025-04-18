# 백준 12851. 숨바꼭질 2
# https://www.acmicpc.net/problem/12851
from collections import deque
def bfs(N, K):
    queue = deque([N])
    visited = [-1] * 100001
    ways = [0] * 100001

    visited[N] = 0
    ways[N] = 1

    while queue:
        cur_x = queue.popleft()

        for next_x in (cur_x - 1, cur_x + 1, 2 * cur_x):
            if 0 <= next_x <= 100000:
                if visited[next_x] == -1:
                    visited[next_x] = visited[cur_x] + 1
                    ways[next_x] = ways[cur_x]
                    queue.append((next_x))
                elif visited[next_x] == visited[cur_x] + 1:
                    ways[next_x] += ways[cur_x]

    return visited[K], ways[K]

def main():
    N, K = map(int, input().split())
    print(*bfs(N, K), sep='\n')

if __name__ == '__main__':
    main()