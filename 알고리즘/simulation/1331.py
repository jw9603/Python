# 백준 1331. 나이트 투어
# https://www.acmicpc.net/problem/1331
################################# 문제 이해 #################################
# 나이트 투어는 체스판에서 나이트가 모든 칸을 정확히 한 번씩 방문하며, 마지막으로 방문하는 칸에서
# 시작점으로 돌아올 수 있는 경로이다.
# 영식이는 6 * 6 체스판 위에서 또 다른 나이트 투어의 경로를 찾으려고 한다.

# 입력: 36개의 줄에 나이트가 방문한 순서대로 입력이 주어진다.
# 출력: 경로가 올바르면 Valid, 그렇지 않으면 Invalid를 출력

# 알고리즘
# 나이트 투어란?
# 이동경로: 상하좌우, 대각선
# 현재칸과 다음칸의 차이: 행과 열의 번호 차이가 ()

################################# 문제 이해 #################################
def seperate_coordinate(num):
    return (ord(num[0]) - ord('A'), int(num[1]) - 1)

def is_valid(sx, sy, nx, ny):
    return abs(sx- nx) == 1 and abs(sy - ny) == 2 or abs(sx - nx) == 2 and abs(sy - ny) == 1

def sol(path):
    valid = True
    visited =[[False] * 6 for _ in range(6)]

    # 방문 체크
    for i in range(36):
        x, y = path[i]
        if visited[y][x]:
            valid = False
            break
        visited[y][x] = True

        if i > 0:
            prev_x, prev_y = path[i - 1]
            if not is_valid(prev_x, prev_y, x, y):
                valid = False
                break
    
    # 시작점과 마지막 점 연결 확인
    if not is_valid(path[0][0], path[0][1], path[-1][0], path[-1][-1]):
        valid = False
    
    # 모든 칸을 한 번씩 방문했는지 확인
    if not all(all(row) for row in visited):
        valid = False

    return "Valid" if valid else "Invalid"
    
def main():
    path = []

    for _ in range(36):
        pos = input().strip()
        x, y = seperate_coordinate(pos)
        path.append((x, y))
    
    print(sol(path))

if __name__ == '__main__':
    main()