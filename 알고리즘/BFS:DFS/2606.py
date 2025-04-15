# 백준 2606. 바이러스
# https://www.acmicpc.net/problem/2606

# 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수를 출력
############################## BFS ##############################
# from collections import defaultdict, deque
# def bfs(graph, start_v):
#     queue = deque([start_v])
#     visited = [start_v]

#     while queue:
#         cur_v = queue.popleft()
#         for next_v in graph[cur_v]:
#             if next_v not in visited:
#                 visited.append(next_v)
#                 queue.append(next_v)
#     return len(visited) - 1

# def main():
#     N = int(input().strip())
#     V = int(input().strip())

#     graph = defaultdict(list)
#     for _ in range(V):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
    
#     print(bfs(graph, 1))

# if __name__ == '__main__':
#     main()
############################## BFS ##############################

############################## DFS ##############################
from collections import defaultdict, deque
def dfs(graph, start_v, visited):
    visited.append(start_v)

    for next_v in graph[start_v]:
        if next_v not in visited:
            dfs(graph, next_v, visited)

def main():
    N = int(input().strip())
    V = int(input().strip())

    graph = defaultdict(list)
    for _ in range(V):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = []
    dfs(graph, 1, visited)
    print(len(visited) - 1)

if __name__ == '__main__':
    main()
############################## DFS ##############################