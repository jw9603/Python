# 백준 2644. 촌수계산
# https://www.acmicpc.net/problem/2644
######################## BFS 풀이 #############################
import sys
from collections import deque, defaultdict
def bfs(graph, n, start, end):
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([(start, 0)])

    while queue:
        cur_v, cur_d = queue.popleft()
        if cur_v == end:
            return cur_d
        
        for next_v in graph[cur_v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append((next_v, cur_d + 1))
    return -1

def main():
    n = int(sys.stdin.readline().strip())
    start, end = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline().strip())

    graph = defaultdict(list)
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)
    
    print(bfs(graph, n, start, end))

if __name__ == '__main__':
    main()
######################## BFS 풀이 #############################

######################## DFS 풀이 #############################
import sys
from collections import deque, defaultdict
def dfs(graph, start, end, visited, cnt):
    visited[start] = True

    if start == end:
        return cnt
    
    for next_v in graph[start]:
        if not visited[next_v]:
            result = dfs(graph, next_v, end, visited, cnt + 1)
            if result != -1:
                return result
    return -1

def main():
    n = int(sys.stdin.readline().strip())
    start, end = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline().strip())

    graph = defaultdict(list)
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [False] * (n + 1)
    print(dfs(graph, start, end, visited, 0))
    
if __name__ == '__main__':
    main()
######################## DFS 풀이 #############################