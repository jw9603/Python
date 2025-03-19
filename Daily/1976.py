# 백준 1976. 여행 가자
# https://www.acmicpc.net/problem/1976
############################## BFS ##############################
import sys
from collections import deque, defaultdict
def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        cur_node = queue.popleft()
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

def main():
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())

    graph = defaultdict(list)
    for i in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        for j in range(N):
            if row[j] == 1:
                graph[i + 1].append(j + 1)
    plans = list(map(int, sys.stdin.readline().split()))
    visited = [False] * (N + 1)

    bfs(plans[0], graph, visited)

    if all(visited[city] for city in plans):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
############################## BFS ##############################

############################## DFS ##############################
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)
def dfs(start, graph, visited):
    visited[start] = True

    for next_node in graph[start]:
        if not visited[next_node]:
            dfs(next_node, graph, visited)
               
def main():
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())

    graph = defaultdict(list)

    for i in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        for j in range(N):
            if row[j] == 1:
                graph[i + 1].append(j + 1)
       
    plans = list(map(int, sys.stdin.readline().split()))

    visited = [False] * (N + 1)
    dfs(plans[0], graph, visited)

    if all(visited[city] for city in plans):
        print("YES")
    else:
        print('NO')

if __name__ == '__main__':
    main()
############################## DFS ##############################