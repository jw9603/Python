# 프로그래머스 - 블록 이동하기
# https://school.programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque
def is_valid(pos, board):
    N = len(board)
    (x1, y1), (x2, y2) = pos
    return (0 <= x1 < N and 0 <= y1 < N and board[x1][y1] == 0 and
            0 <= x2 < N and 0 <= y2 < N and board[x2][y2] == 0)
    
def get_next(cur, board):
    (x1, y1), (x2, y2) = cur
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    next_positions = []
    
    # 1. 상, 하, 좌, 우 이동
    for dx, dy in directions:
        next_x1, next_y1, next_x2, next_y2 = x1 + dx, y1 + dy, x2 + dx, y2 + dy
        if is_valid(((next_x1, next_y1), (next_x2, next_y2)), board):
            next_positions.append(((next_x1, next_y1), (next_x2, next_y2)))
            
    # 2. 회전
    if x1 == x2: # 위 아래로 회전
        for d in [1, -1]:
            if 0 <= x1 + d < len(board) and board[x1 + d][y1] == 0 and board[x2 + d][y2] == 0:
                next_positions.append(((x1, y1), (x1 + d, y1)))
                next_positions.append(((x2, y2), (x2 + d, y2)))
    if y1 == y2: # 왼쪽, 오른쪽으로 회전
        for d in [1, -1]:
            if 0 <= y1 +d < len(board) and board[x1][y1 + d] == 0 and board[x2][y2 + d] == 0:
                next_positions.append(((x1, y1), (x1, y1 + d)))
                next_positions.append(((x2, y2), (x2, y2 + d)))
                
    return next_positions
            
def solution(board):
    N = len(board)
    start = ((0, 0), (0, 1))
    queue = deque([(start, 0)])
    
    visited = set()
    visited.add(frozenset(start))
    
    while queue:
        cur, cur_t = queue.popleft()
        (x1, y1), (x2, y2) = cur
        if (x1 == N - 1 and y1 == N - 1) or (x2 == N - 1 and y2 == N - 1):
            return cur_t
        
        for next_pos in get_next(cur, board):
            frozen_next = frozenset(next_pos)
            if frozen_next not in visited:
                visited.add(frozen_next)
                queue.append((next_pos, cur_t + 1))
    return 0