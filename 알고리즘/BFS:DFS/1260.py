# 백준 1260. DFS와 BFS
# https://www.acmicpc.net/workbook/view/22734
from collections import defaultdict, deque
def bfs(graph, start):
    visited = []
    visited.append(start)
    queue = deque([start])

    while queue:
        cur_v = queue.popleft()
        for next_v in sorted(graph[cur_v]):
            if next_v not in visited:
                visited.append(next_v)
                queue.append(next_v)
    
    return visited

def dfs(graph, start, visited):
    visited.append(start)

    for next_v in sorted(graph[start]):
        if next_v not in visited:
            dfs(graph, next_v, visited)
    

def main():
    N, M, V = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = []
    dfs(graph, V, visited)
    print(*visited)
    print(*bfs(graph, V))

if __name__ == '__main__':
    main()