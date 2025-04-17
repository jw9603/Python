# 백준 11724. 연결 요소의 개수
# https://www.acmicpc.net/problem/11724
#################### 문제 이해 ####################
# 방항없는 그래프가 주어졌을 때, 연결 요소(Connected Component)의 개수를 구해라.

# 입력
# 정점의 개수 N과 간선의 개수 M이 주어진다.
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (u와 v는 서로 다르다)

# 시작점이 있다면 그 시작점과 연결된 요소들끼리의 개수를 카운트
# 즉, 모든 노드에 대해 BFS를 해보는 것

#################### 문제 이해 ####################
############################ BFS ###############################
from collections import defaultdict, deque
def bfs(start_v, graph, visited):
    visited[start_v] = True
    queue = deque([start_v])

    while queue:
        cur_v = queue.popleft()

        for next_v in graph[cur_v]:
            if not visited[next_v]:
                queue.append(next_v)
                visited[next_v] = True
            
def count_connected_component(N, graph):
    cnt = 0
    visited = [False] * (N + 1)

    for v in range(1, N + 1):
        if not visited[v]:
            bfs(v, graph, visited)
            cnt += 1
    
    return cnt

def main():
    N, M = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    print(count_connected_component(N, graph))

if __name__ == '__main__':
    main()
############################ BFS ###############################
############################ DFS ###############################
from collections import defaultdict
def dfs(start_v, graph, visited):
    visited[start_v] = True

    for next_v in graph[start_v]:
        if not visited[next_v]:
            dfs(next_v, graph, visited)

def count_connected_component(N, graph):
    cnt = 0
    visited = [False] * (N + 1)

    for v in range(1, N + 1):
        if not visited[v]:
            dfs(v, graph, visited)
            cnt += 1
    
    return cnt

def main():
    N, M = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    print(count_connected_component(N, graph))

if __name__ == '__main__':
    main()
############################ DFS ###############################