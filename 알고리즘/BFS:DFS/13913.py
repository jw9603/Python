# 백준 13913. 숨바꼭질 4
# https://www.acmicpc.net/problem/13913
from collections import deque
def bfs(N, K):
    queue = deque([N])
    visited = [-1] * 100001
    visited[N] = 0
    prev = [-1] * 100001
    prev[N] = N

    while queue:
        cur_v = queue.popleft()

        for next_v in [cur_v - 1, cur_v + 1, 2 * cur_v]:
            if 0 <= next_v <= 100000 and visited[next_v] == -1:
                visited[next_v] = visited[cur_v] + 1
                queue.append((next_v))
                prev[next_v] = cur_v
    
    return visited[K], prev

def reconstruct(N, K, prev):
    path = []
    curr = K

    while curr!= N:
        path.append(curr)
        curr = prev[curr]
    path.append(N)
    path.reverse()
    
    return path
    
def main():
    N, K = map(int, input().split())

    a, b = bfs(N, K)
    b = reconstruct(N, K, b)
    print(a)
    print(*b)

if __name__ == '__main__':
    main()