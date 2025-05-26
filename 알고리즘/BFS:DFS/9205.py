# 백준 9205. 맥주 마시면서 걸어가기
# https://www.acmicpc.net/problem/9205
################################ 문제 이해 ################################
# 맥주를 마시면서 걸어가기로 했다.
# 상근이네 집에서 출발, 맥주 한 박스를 들고 출발, 맥주 한 박스에는 맥주가 20개 들어있음
# 50미터에 1병, 즉, 50미터를 가려면 그 직전에 맥주 한 병을 마셔야 한다.
# 목표: 상근이의 집 -> 페스티벌,
# 맥주는 최대 20병을 들고 다닐 수 있음, 편의점을 들르면 맥주를 살 수 잇음.
# 편의점, 상근이네 집, 페스티벌의 좌표가 주어진다.
# 페스티벌에 도착할 수 있는지 구하는 프로그램을 작성

# 입력
# 첫째 줄에 테스트 케이스의 개수 t가 주어진다.
# 각 테스트 케이스의 첫째 줄에는 맥주를 파는 편의점의 개수 n이 주어진다.
# 다음 n + 2개의 줄에는 상근이집, 편의점, 페스티벌 좌표

# 알고리즘
# 맥주를 마셔야 걸을수 있고, 편의점의 개수는 제한적이다.
# 따라서, 최단거리 -> BFS 사용
# BFS에서 만약 현재 위치에서 페스티벌까지의 거리가 50m * 20개 == 1000m 이하이면 바로 가능
# 아니라면, 현재위치와 편의점들간의 거리를 계속 업데이트

################################ 문제 이해 ################################
from collections import deque
def can_reach_festival(n, house, stores, festival):
    queue = deque([house])
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
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        house = list(map(int, input().split()))
        stores = [list(map(int, input().split())) for _ in range(n)]
        festival = list(map(int, input().split()))
        print(can_reach_festival(n, house, stores, festival))

if __name__ == '__main__':
    main()