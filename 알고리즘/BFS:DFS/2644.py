# 백준 2644. 촌수계산
# https://www.acmicpc.net/problem/2644
############################# 문제 이해 #############################
# 부모와 자식 사이를 1촌으로 정의
# 나 -> 아빠 -> 할아버지 , 나와 할아버지는 2촌, 
# 즉 두 노드간의 연결의 길이를 구하는 문제

############################# 문제 이해 #############################
############################# BFS #############################
# from collections import deque, defaultdict
# def bfs(n, start, end, graph):
#     queue = deque([(start ,0)])
#     visited = [False] * (n + 1)
#     visited[start] = True

#     while queue:
#         cur_v, cur_chonsu = queue.popleft()

#         if cur_v == end:
#             return cur_chonsu
        
#         for next_v in graph[cur_v]:
#             if not visited[next_v]:
#                 visited[next_v] = True
#                 queue.append((next_v, cur_chonsu + 1))
    
#     return -1

# def main():
#     n = int(input().strip())
#     a, b = map(int, input().split())
#     m = int(input().strip())
#     graph = defaultdict(list)

#     for _ in range(m):
#         # x: 부모, y: 자식
#         x, y = map(int, input().split())
#         graph[x].append(y)
#         graph[y].append(x)
    
#     print(bfs(n, a, b, graph))

# if __name__ == '__main__':
#     main()
############################# BFS #############################
############################# DFS #############################
from collections import defaultdict
def dfs(graph, start, end, visited, cnt):
    visited.append(start)

    if start == end:
        return cnt
    
    for next_v in graph[start]:
        if next_v not in visited:
            result = dfs(graph, next_v, end, visited, cnt + 1)
            if result != -1:
                return result
    return -1

def main():
    n = int(input().strip())
    a, b = map(int, input().split())
    m = int(input().strip())
    graph = defaultdict(list)

    for _ in range(m):
        # x: 부모, y: 자식
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = []
    print(dfs(graph, a, b, visited, 0))

if __name__ == '__main__':
    main()
############################# DFS #############################