# 백준 15683. 감시
# https://www.acmicpc.net/problem/15683
import sys

def watch_area(office, x, y, directions):
    tmp_office = [row[:] for row in office]
    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        while 0 <= next_x < len(office) and 0 <= next_y < len(office[0]):
            if tmp_office[next_x][next_y] == 6:
                break
            if tmp_office[next_x][next_y] == 0:
                tmp_office[next_x][next_y] = "#"
            next_x += dx
            next_y += dy
    return tmp_office

def dfs(depth, office, cctvs, cctv_modes):
    global min_cnt
    
    if depth == len(cctvs):
        count = sum(row.count(0) for row in office)
        min_cnt = min(count, min_cnt)
        return
    
    x, y, cctv_types = cctvs[depth]
    
    for directions in cctv_modes[cctv_types]:
        
        new_office = watch_area(office, x, y, directions)
        dfs(depth + 1, new_office, cctvs, cctv_modes)
        
def main():
    global min_cnt
    N, M = map(int, sys.stdin.readline().split())
    
    cctv_modes = {
    1: [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]],  # →, ←, ↓, ↑
    2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],  # ↔, ↕
    3: [[(0, 1), (-1, 0)], [(0, 1), (1, 0)], [(0, -1), (1, 0)], [(0, -1), (-1, 0)]],  # ┐ ┘ └ ┌
    4: [[(0, 1), (0, -1), (-1, 0)], [(0, 1), (0, -1), (1, 0)], [(1, 0), (-1, 0), (0, -1)], [(1, 0), (-1, 0), (0, 1)]],  # 3방향
    5: [[(0, 1), (0, -1), (1, 0), (-1, 0)]]  # 전 방향 감시
    }
    
    office = []
    cctvs = []
    for i in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        office.append(row)
        for j in range(M):
            if 1 <= row[j] <= 5:
                cctvs.append((i, j, row[j]))
    
    min_cnt = float('inf')
    
    dfs(0, office, cctvs, cctv_modes)
    print(min_cnt)
main()