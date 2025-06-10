# 백준 8911. 거북이
# https://www.acmicpc.net/problem/8911
############################# 문제 이해 #############################
# 2차원 평면 위에서 움직일 수 있는 거북이 로봇, 거북이에게 내릴 수 있는 명령은 다음 4가지
# F: 앞, B: 뒤, L: 왼쪽으로 90도, R: 오른쪽으로 90도
# 명령을 나열한 것을 거북이 로봇의 컨트롤 프로그램
# 상근이는 자신의 컨트롤 프로그램으로 거북이가 이동한 영역을 계산
# 거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형의 넓이를 계산

# 거북이는 처음에 (0, 0)에 위치하고 북쪽

# 알고리즘
# (0, 0) -> 한 눈금 뒤로 -> (0, -1)
# (0, 1)
############################# 문제 이해 #############################
def simulate(command):
    # 북, 서, 남, 동
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direction = 0
    x, y = 0, 0
    max_x, max_y, min_x, min_y = 0, 0, 0, 0

    for cmd in command:
        if cmd == 'F':
            x += dx[direction]
            y += dy[direction]
        elif cmd == 'B':
            x -= dx[direction]
            y -= dy[direction]
        elif cmd == 'L':
            direction = (direction + 3) % 4
        else:
            direction = (direction + 1) % 4
        
        min_x, min_y = min(min_x, x), min(min_y, y)
        max_x, max_y = max(max_x, x), max(max_y, y)
    
    return abs(max_x - min_x) * abs(max_y - min_y)
        
def main():
    T = int(input().strip())

    for _ in range(T):
        command = list(input().strip())
        print(simulate(command))

if __name__ == '__main__':
    main()