# 백준 1389. 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389
import sys
from collections import deque, defaultdict
def bfs(start, N, graph):
    queue = deque([(start, 0)])
    visited = [False] * (N + 1)
    visited[start] = True
    total_distance = 0

    while queue:
        cur_friend, cur_step = queue.popleft()
        total_distance += cur_step

        for next_friend in graph[cur_friend]:
            if not visited[next_friend]:
                visited[next_friend] = True
                queue.append((next_friend, cur_step + 1))
    return total_distance

def main():
    N, M = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    min_kevin = float('inf')
    answer = -1
    for i in range(1, N + 1):
        kevin_number = bfs(i, N, graph)
        if kevin_number < min_kevin:
            min_kevin = kevin_number
            answer = i
    
    print(answer)

if __name__ == '__main__':
    main()