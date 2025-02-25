# 백준 2644. 촌수 계산
# https://www.acmicpc.net/problem/2644

############################# BFS ################################
import sys
from collections import deque, defaultdict
def bfs(n, start, target, graph):
    visited = [False] * (n + 1)
    queue = deque([(start, 0)])
    visited[start] = True
    while queue:
        cur_v, cur_cnt = queue.popleft()
        
        if cur_v == target:
            return cur_cnt
        for next_v in graph[cur_v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append((next_v, cur_cnt + 1))
    return -1

def main():
    n = int(sys.stdin.readline().strip())
    a, b = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline().strip())
    graph = defaultdict(list)
    
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)
    
    print(bfs(n=n, start=a, target=b, graph=graph))
main()
############################# BFS ################################

############################# DFS ################################
import sys
from collections import defaultdict

def dfs(start, target, graph, visited, cnt):
    visited[start] = True
    if start == target:
        return cnt
    for next_v in graph[start]:
        if not visited[next_v]:
            result = dfs(next_v, target, graph, visited, cnt + 1)
            if result != -1:
                return result
    return -1
def main():
    n = int(sys.stdin.readline().strip())
    a, b = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline().strip())
    graph = defaultdict(list)
    
    for _ in range(m):
        # x는 y의 부모
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [False] * (n + 1)
    print(dfs(start=a, target=b, graph=graph, visited=visited, cnt=0))
main()
############################# DFS ################################