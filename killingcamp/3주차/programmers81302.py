# 프로그래머스 거리두기 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/81302
from collections import deque

def check(room):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    N = 5
    for i in range(N):
        for j in range(N):
            if room[i][j] != "P":
                continue
            queue = deque([(i, j, 0)])
            visited = [[False] * N for _ in range(N)]
            visited[i][j] = True
            
            while queue:
                cur_x, cur_y, cur_d = queue.popleft()
                if cur_d >= 2:
                    continue
                for dx, dy in directions:
                    next_x, next_y = cur_x + dx, cur_y + dy
                    
                    if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        if room[next_x][next_y] == 'P':
                            return 0
                        elif room[next_x][next_y] == 'O':
                            queue.append((next_x, next_y, cur_d + 1))
    return 1      

def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer
