# 백준 1260.DFS와 BFS
# https://www.acmicpc.net/problem/1260
######################## 문제 이해########################
# 그래프를 DFS, BFS로 탐색한 결과를 출력하는 프로그램을 작성해라.
# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
# 정점 번호는 1부터 N까지의 자연수로 표현

# 입력:
# 첫째 줄에 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
# 둘째 줄부터 M개의 줄에 간선이 연결하는 두 정점의 번호가 주어진다.

# 출력:
# 첫째 줄에 DFS를 수행한 결과를, 둘째 줄에 BFS를 수행한 결과를 출력한다.

######################## 문제 이해########################
from collections import deque, defaultdict

def bfs(graph, start):
    visited = [start]
    queue = deque([start])
   
    while queue:
        cur_node = queue.popleft()
        
        for next_node in sorted(graph[cur_node]):
            if next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)

    return visited

def dfs(graph, start, visited):
    visited.append(start)
    
    for next_node in sorted(graph[start]):
        if next_node not in visited:
            dfs(graph, next_node, visited)
    
    return visited
    
def main():
    N, M, V = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    print(*dfs(graph, V, []))
    print(*bfs(graph, V))   

if __name__ == "__main__":
    main()