# 백준 2606. 바이러스
# https://www.acmicpc.net/problem/2606
##################################### 문제 이해 #####################################
# 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크상에 연결되어 있는 모든 컴퓨터는 바이러스에 걸림
# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해
# 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성해라!

# 입력
# 첫째 줄에는 컴퓨터의 수가 주어짐
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터의 쌍 수 -> 에지 개수

# 출력
# 1번 컴퓨터가 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력

# 알고리즘:
# Number of islands 문제라고 볼 수 있다.
# 즉 1번 노드와 연결된 노드의 개수를 구해야하기 때문에 1번 노드로부터 BFS or DFS를 수행

##################################### 문제 이해 #####################################
# 1. BFS
# from collections import defaultdict, deque
# def bfs(graph, start_v):
#     queue = deque([start_v])
#     visited = {start_v}

#     while queue:
#         cur_v = queue.popleft()
#         for next_v in graph[cur_v]:
#             if next_v not in visited:
#                 visited.add(next_v)
#                 queue.append(next_v)
    
#     return len(visited) - 1
    
# def main():
#     N = int(input().strip())
#     M = int(input().strip())
#     graph = defaultdict(list)

#     for _ in range(M):
#         u, v = map(int, input().split())
#         graph[u].append(v)
#         graph[v].append(u)
    
#     print(bfs(graph, 1))

# if __name__ == '__main__':
#     main()

# 2. DFS
from collections import defaultdict
def dfs(graph, vertex, visited):
    visited.add(vertex)

    for next_v in graph[vertex]:
        if next_v not in visited:
            dfs(graph, next_v, visited)
    
    return visited

def main():
    N = int(input().strip())
    M = int(input().strip())
    graph = defaultdict(list)

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    print(len(dfs(graph, 1, set())) - 1)

if __name__ == '__main__':
    main()