# 백준 9079. 동전 게임
# https://www.acmicpc.net/problem/9079
import sys
from collections import deque
T = int(sys.stdin.readline().strip())

def invert_string(coins):
    return ''.join([''.join(row) for row in coins])

def flip(coins_str, indices):
    coin_list = list(coins_str)
    for idx in indices:
        coin_list[idx] = 'H' if coin_list[idx] == 'T' else 'T'
    return ''.join(coin_list)


def sol(coins):
    initial_state = invert_string(coins)
    

    if initial_state == 'HHHHHHHHH' or initial_state == 'TTTTTTTTT':
        return 0
    
    flip_indices = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    queue = deque([(initial_state, 0)])
    visited = set()
    visited.add(initial_state)    
    while queue:
        curr_state, steps = queue.popleft()
        
        for indices in flip_indices:
            new_state = flip(curr_state, indices)
            if new_state ==  'HHHHHHHHH' or new_state == 'TTTTTTTTT':
                return steps + 1
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, steps + 1))
    return -1

for _ in range(T):
    coins = [list(sys.stdin.readline().split()) for _ in range(3)]
    print(sol(coins))