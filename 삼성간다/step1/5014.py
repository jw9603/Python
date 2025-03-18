# 백준 5014. 스타트링크
# https://www.acmicpc.net/problem/5014
import sys
from collections import deque
def bfs(start, end, u, d, f):
    queue = deque([(start, 0)])
    visited = [False] * 1000001
    visited[start] = True
    

    while queue:
        cur_x, cur_click = queue.popleft()
        if cur_x == end:
            return cur_click
        for next_x in [cur_x + u, cur_x - d]:
            if 1 <= next_x <= f and not visited[next_x]:
                visited[next_x] = True
                queue.append((next_x, cur_click + 1))
    return "use the stairs"

def main():
    F, S, G, U, D = map(int, sys.stdin.readline().split())
    # S: start, G: end, 
    print(bfs(S, G, U, D, F))

if __name__ == '__main__':
    main()