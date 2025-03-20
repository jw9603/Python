# 백준 1525. 퍼즐
# https://www.acmicpc.net/problem/1525
import sys
from collections import deque
def bfs(data):
    target = "123456780"
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(data, data.index("0"), 0)]) 
    visited = set()
    visited.add(data)

    while queue:
        cur_data, cur_idx, cur_steps = queue.popleft()

        if cur_data == target:
            return cur_steps
        
        x, y = cur_idx // 3, cur_idx % 3
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy

            if 0 <= next_x < 3 and 0 <= next_y < 3:
                next_idx = next_x * 3 + next_y
                next_data = list(cur_data)

                next_data[cur_idx], next_data[next_idx] = next_data[next_idx], next_data[cur_idx]
                next_data = ''.join(next_data)

                if next_data not in visited:
                    visited.add(next_data)
                    queue.append((next_data, next_idx, cur_steps + 1))
    return -1

def main():
    data = []
    for _ in range(3):
        row = sys.stdin.readline().split()
        row = ''.join(row)
        data.append(row)
    data = ''.join(data)
    print(bfs(data))

if __name__ == '__main__':
    main()