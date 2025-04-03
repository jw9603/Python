# 백준 15683. 감시
# https://www.acmicpc.net/problem/15683
def watch_area(x, y, office, directions):
    tmp_office = [row[:] for row in office]

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        while 0 <= next_x < len(office) and 0 <= next_y < len(office[0]):
            if tmp_office[next_x][next_y] == 6:
                break
            if tmp_office[next_x][next_y] == 0:
                tmp_office[next_x][next_y] = '#'
            
            next_x += dx
            next_y += dy
    
    return tmp_office

def dfs(depth, office, cctvs, cctv_modes):
    global min_size

    if depth == len(cctvs):
        cnt = sum(row.count(0) for row in office)
        min_size = min(min_size, cnt)
        return
    
    x, y, cctv_types = cctvs[depth]

    for directions in cctv_modes[cctv_types]:
        new_area = watch_area(x, y, office, directions)
        dfs(depth + 1, new_area, cctvs, cctv_modes)


def main():
    global min_size
    N, M = map(int, input().split())

    office, cctvs = [], []
    for i in range(N):
        row = list(map(int, input().split()))
        office.append(row)
        for j in range(M):
            if 1 <= row[j] <= 5:
                cctvs.append((i, j, row[j]))

    min_size = float('inf')
    cctv_modes = {
        1 : [[(0, 1)], [(-1, 0)], [(1, 0)], [(0, -1)]],
        2 : [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
        3 : [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
        4 : [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
        5 : [[(0, 1), (1, 0), (0, -1), (-1, 0)]],
    }

    dfs(0, office, cctvs, cctv_modes)

    print(min_size)

if __name__ == '__main__':
    main()