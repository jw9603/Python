# 백준 14502. 연구소
# https://www.acmicpc.net/problem/14502
##################################### 백트래킹 #####################################
from collections import deque
def bfs(N, M, lab, virus_spaces):
    queue = deque(virus_spaces)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
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

def count_safe_areas(depth, start, lab, empty_spaces, virus_spaces, N, M):
    global max_safe_areas

    if depth == 3:
        max_safe_areas = max(max_safe_areas, bfs(N, M, lab, virus_spaces))
        return
    
    for i in range(start, len(empty_spaces)):
        x, y = empty_spaces[i]
        lab[x][y] = 1
        count_safe_areas(depth + 1, i + 1, lab, empty_spaces, virus_spaces, N, M)
        lab[x][y] = 0

def main():
    global max_safe_areas
    N, M = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(N)]

    empty_spaces = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
    virus_spaces = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 2]

    max_safe_areas = 0

    count_safe_areas(0, 0, lab, empty_spaces, virus_spaces, N, M)

    print(max_safe_areas)

if __name__ == '__main__':
    main()
##################################### 백트래킹 #####################################

##################################### 백트래킹 #####################################
from collections import deque
from itertools import combinations
def bfs(N, M, lab, virus_spaces):
    queue = deque(virus_spaces)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
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

def count_safe_areas(lab, N, M):
    empty_spaces = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
    virus_spaces = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 2]
    max_safe_areas = 0

    for walls in combinations(empty_spaces, 3):

        for x, y in walls:
            lab[x][y] = 1

        max_safe_areas = max(max_safe_areas, bfs(N, M, lab, virus_spaces))

        for x, y in walls:
            lab[x][y] = 0
    
    return max_safe_areas

def main():
    N, M = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(N)]

    print(count_safe_areas(lab, N, M))

if __name__ == '__main__':
    main()
##################################### 백트래킹 #####################################