# 백준 15685. 드래곤 커브
# https://www.acmicpc.net/problem/15685
def main():
    N = int(input().strip())

    visited = [[False] * 101 for _ in range(101)]

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for _ in range(N):
        x, y, d, g = map(int, input().split())

        directions = [d]
        for _ in range(g):
            for i in reversed(range(len(directions))):
                directions.append((directions[i] + 1) % 4)
        
        visited[y][x] = True
        for direction in directions:
            x += dx[direction]
            y += dy[direction]

            if 0 <= x <= 100 and 0 <= y <= 100:
                visited[y][x] = True
    
    cnt = 0
    for i in range(100):
        for j in range(100):
            if visited[i][j] and visited[i + 1][j] and visited[i][j + 1] and visited[i + 1][j + 1]:
                cnt += 1
    
    print(cnt)

if __name__ == '__main__':
    main()     

