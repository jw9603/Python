# 백준 5014. 스타트링크
# https://www.acmicpc.net/problem/5014
############################# 문제 이해 #############################
# 총 F층으로 이루어진 고층 건물에 사무실이 있고, 스타트링크가 있는 곳의 위치는 G층이다.
# 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.

# 엘리베이터 버튼은 2개
# U 버튼: 위로 U층을 가는 버튼
# D 버튼: 아래로 D층을 가는 버튼

# 강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구해라.
# 만약 G층에 갈 수 없다면 "use the stairs"를 출력
############################# 문제 이해 #############################
from collections import deque
def sol(F, start, end, u, d):
    '''
    총 F층
    지금 있는 곳: S
    목표: G
    '''
    visited = [False] * (F + 1)
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        cur_v, cur_click = queue.popleft()

        if cur_v == end:
            return cur_click
        
        for next_v in [cur_v + u, cur_v - d]:
            if 1 <= next_v <= F and not visited[next_v]:
                visited[next_v] = True
                queue.append((next_v, cur_click + 1))
    
    return "use the stairs"

def main():
    F, S, G, U, D = map(int, input().split())

    print(sol(F, S, G, U, D))

if __name__ == '__main__':
    main()