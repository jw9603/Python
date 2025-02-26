# 백준 14502. 연구소
# https://www.acmicpc.net/problem/14502
import sys
from collections import deque
from itertools import combinations

def bfs(lab, virus_spaces, N, M):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque(virus_spaces)
    tmp_lab = [row[:] for row in lab]
    while queue:
        cur_x, cur_y = queue.popleft()
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < N and 0 <= next_y < M:
                if tmp_lab[next_x][next_y] == 0:
                    tmp_lab[next_x][next_y] = 2
                    queue.append((next_x, next_y))
                
    return sum(row.count(0) for row in tmp_lab)
    
def get_max_safe_areas(N, M, lab):
    empty_spaces = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
    virus_spaces = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 2]
    max_safe_area = 0
    
    for walls in combinations(empty_spaces, 3):
        
        for x, y in walls:
            lab[x][y] = 1
        
        max_safe_area = max(max_safe_area, bfs(lab, virus_spaces, N, M))
        
        for x, y in walls:
            lab[x][y] = 0
            
    return max_safe_area

def main():
    N, M = map(int, sys.stdin.readline().split())
    lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    print(get_max_safe_areas(N=N, M=M, lab=lab))
main()
