# 백준 7562. 나이트의 이동
# https://www.acmicpc.net/problem/7562
import sys
from collections import deque

def bfs(l, start, target):
    sx, sy = start
    tx, ty = target
    
    if (sx, sy) == (tx, ty):
        return 0
    
    directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    
    visited = [[False] * l for _ in range(l)]
    queue = deque([(sx, sy, 0)])
    visited[sx][sy] = True
    
    while queue:
        cur_x, cur_y, cur_cnt = queue.popleft()

        if (cur_x, cur_y) == (tx, ty):
            return cur_cnt
        
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
        
            if 0 <= next_x < l and 0 <= next_y < l and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y, cur_cnt + 1))


def main():
    T = int(sys.stdin.readline().strip())
    
    for _ in range(T):
        l = int(sys.stdin.readline().strip())
        sx, sy = map(int, sys.stdin.readline().split())
        tx, ty = map(int, sys.stdin.readline().split())
        
        print(bfs(l=l, start=(sx, sy), target=(tx, ty)))
main()