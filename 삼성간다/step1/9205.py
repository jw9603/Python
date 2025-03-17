# 백준 9205. 맥주 마시면서 걸어가기
# https://www.acmicpc.net/problem/9205
import sys
from collections import deque

def can_reach_festival():
    queue = deque([home])
    visited = set()

    while queue:
        cur_x, cur_y = queue.popleft()

        if abs(cur_x - festival[0]) + abs(cur_y - festival[1]) <= 1000:
            return "happy"
        
        for i in range(n):
            if i not in visited:
                next_x, next_y = stores[i]
                if abs(cur_x - next_x) + abs(cur_y - next_y) <= 1000:
                    visited.add(i)
                    queue.append((next_x, next_y))
    return "sad"

def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        global n, home, stores, festival
        n = int(sys.stdin.readline().strip()) # 편의 점의 개수
        home = map(int, sys.stdin.readline().split())
        stores = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
        festival = list(map(int, sys.stdin.readline().split()))
        print(can_reach_festival())

if __name__ == '__main__':
    main()