# 게임 개발
import sys
n, m = map(int, sys.stdin.readline().split())

x, y, direction = map(int, sys.stdin.readline().split())

d = [[0] * m for _ in range(n)]
d[x][y] = 1

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin().readline().split())))
    
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction 
    direction -= 1
    if direction == -1:
        direction = 3

cnt = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + y[direction]
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and arr[nx][ny] ==0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    # 네 방향으로 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(cnt)