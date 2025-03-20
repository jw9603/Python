# 백준 9019. DSLR
# https://www.acmicpc.net/problem/9019
import sys
from collections import deque
def bfs(A, B):
    queue = deque([(A, [])])
    visited = [False] * 10000
    visited[A] = True

    while queue:
        cur_val, commands = queue.popleft()

        if cur_val == B:
            return ''.join(commands)

        # D
        next_val = (cur_val * 2) % 10000
        if not visited[next_val]:
            visited[next_val] = True
            queue.append((next_val, commands + ["D"]))
        
        # S
        next_val = (cur_val - 1) if cur_val != 0 else 9999
        if not visited[next_val]:
            visited[next_val] = True
            queue.append((next_val, commands + ["S"]))
        
        # L
        next_val = (cur_val % 1000) * 10 + cur_val // 1000
        if not visited[next_val]:
            visited[next_val] = True
            queue.append((next_val, commands + ["L"]))
        
        # R
        next_val = (cur_val % 10) * 1000 + cur_val // 10
        if not visited[next_val]:
            visited[next_val] = True
            queue.append((next_val, commands + ["R"]))
    
def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        A, B = map(int, sys.stdin.readline().split())
        print(bfs(A, B))

if __name__ == '__main__':
    main()