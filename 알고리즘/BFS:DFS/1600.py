# 백준 1600. 말이 되고픈 원숭이
# https://www.acmicpc.net/problem/1600 
############################# 문제 이해 #############################
# 동물원에서 원숭이 탈출, 원숭이는 말이 되기를 간절히 원했다.
# 원숭이는 말의 움직임을 유심히 살펴보고 그대로 따라 하기로 하였다.
# 말은 격자판에서 체스의 나이트와 같은 이동방식을 가진다. # 말은 장애물을 뛰어 넘을 수 있다.

# 말은 저렇게 움직일 수 있지만 원숭이는 능력이 부족해서 총 K번만 위와 같이 움직일 수 있고,
# 그외에는 그냥 인접한 칸으로만 움직일 수 있다. (인접=상하좌우)
# (0, 0)에서 시작해서 맨 오른쪽 아래까지 가야한다.
# 인접한 칸으로 한 번 움직이는 것, 말의 움직임으로 한 번 움직이는 것, 모두 한 번의 동작으로 친다.
# 격자판이 주어졌을 때, 원숭이가 최소한의 동작으로 시작지점에서 도차지점까지 

# 입력
# 첫째 줄에 정수 K가 주어진다. 둘째 줄에 격자판의 가로 길이 W, 세로 길이 H가 주어진다.
# 0은 평지, 1은 장애물,
# 출력
# 첫째 줄에 원숭이의 동작수의 최솟값, 아니면 -1

# 알고리즘

# 말은 (1,2) ,(2, 1) 이런식으로 인접한 칸보다 이동 거리가 큼, 하지만 말처럼 움직이는
# 횟수는 총 K번만 가능하다. 그렇다고 말의 이동을 더 우선순위로 두면 안된다.
# 이것은 그리디로 풀 수 없다. 왜냐하면 말의 이동방식을 먼저햇는데 더이상 방법이 없을수도 있다.
# 따라서 동일하게 적용시켜야 한다. 즉, 현재 위치에서 말방법, 인접방법 모두 측정

# 원숭이의 동작수가 최소여야 한다. 그리고 총 K번 이동해야 하므로,
# 현재 위치가 K를 썻는지 안썼는지 체크를 해야 한다. K번은 무조건 해야하니까
############################# 문제 이해 #############################
from collections import deque
def min_monkey_action(k, w, h, grid):
    queue = deque([(0, 0, 0, 0)]) # x, y, steps, k
    visited = [[[False] * (k + 1) for _ in range(w)] for _ in range(h)]
    visited[0][0][0] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    knight_directions = [(-2, -1), (-2, 1), (1, -2), (-1, 2), (1, 2), (-1, -2), (2, -1), (2, 1)]

    while queue:
        cur_x, cur_y, cur_step, cur_k = queue.popleft()

        if cur_x == h - 1 and cur_y == w - 1:
            return cur_step
        
        # 1. 인접한 칸으로 움직이는 방법
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < h and 0 <= next_y < w:
                if not visited[next_x][next_y][cur_k] and grid[next_x][next_y] == 0:
                    visited[next_x][next_y][cur_k] = True
                    queue.append((next_x, next_y, cur_step + 1, cur_k))
        
        # 2. 말처럼 움직이는 방법
        if cur_k < k:
            for dx, dy in knight_directions:
                next_x, next_y = cur_x + dx, cur_y + dy
                if 0 <= next_x < h and 0 <= next_y < w:
                    if not visited[next_x][next_y][cur_k + 1] and grid[next_x][next_y] == 0:
                        visited[next_x][next_y][cur_k + 1] = True
                        queue.append((next_x, next_y, cur_step + 1, cur_k + 1))
    
    return -1

def main():
    K = int(input().strip())
    W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]

    print(min_monkey_action(K, W ,H, grid))

if __name__ == '__main__':
    main()