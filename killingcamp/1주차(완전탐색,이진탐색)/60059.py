# 프로그래머스 - 자물쇠와 열쇠
# https://school.programmers.co.kr/learn/courses/30/lessons/60059

def rotate(arr):
   # [[1, 2],
   # [5, 4]] -> 90도 회전 : [[5, 1], [4, 2]]
        
    return list(zip(*arr[::-1]))

def is_unlock(expanded_lock, lock_start, lock_end):
    for i in range(lock_start, lock_end):
        for j in range(lock_start, lock_end):
            if expanded_lock[i][j] != 1:
                return False
    return True
    
def push_key(expanded_lock, key, x, y, backtrack=True):
    m = len(key)

    for i in range(m):
        for j in range(m):
            expanded_lock[x + i][y + j] += key[i][j] if backtrack else -key[i][j]
            
def solution(key, lock):
    # key의 돌기 부분(1)이 lock의 홈 부분(0)과 만나야 함.
    n, m = len(lock), len(key)
    
    lock_size = n + 2 * (m - 1)
    start, end = m - 1, m - 1 + n
    
    expanded_lock = [[0] * lock_size for _ in range(lock_size)] # key가 움직여야 하니까!
    for i in range(n):
        for j in range(n):
            expanded_lock[i + m - 1][j + m - 1] = lock[i][j]

    # 회전(90, 180, 270, 0), 이동(상, 하, 좌, 우)
    for _ in range(4):
        key = rotate(key)
        
        for x in range(lock_size - m + 1):
            for y in range(lock_size - m + 1):
                push_key(expanded_lock, key, x, y, True)
                if is_unlock(expanded_lock, start, end):
                    return True
                push_key(expanded_lock, key, x, y, False)
    return False
                
if __name__ == '__main__':
    key, lock = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(f"Result: {solution(key=key, lock=lock)}")