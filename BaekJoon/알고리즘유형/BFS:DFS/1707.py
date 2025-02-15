# 백준 1707. 이분 그래프
# https://www.acmicpc.net/problem/1707

############################# BFS 풀이 #################################
import sys
from collections import defaultdict, deque

def main():
    K = int(sys.stdin.readline().strip())
    
    def bfs(v, graph):
        colors = [-1] * (v + 1) # -1: 미방문 상태, 0과 1: 두 개의 그룹
        
        for start in range(1, v + 1):
            if colors[start] == -1:
                queue = deque([start])
                colors[start] = 0
                
                while queue:
                    cur_node = queue.popleft()
                    
                    for next_node in graph[cur_node]:
                        if colors[next_node] == -1:
                            colors[next_node] = 1 - colors[cur_node]
                            queue.append(next_node)
                        elif colors[next_node] == colors[cur_node]:
                            return "NO"
        return "YES"
    for _ in range(K):
        V, E = map(int, sys.stdin.readline().split())
        
        graph = defaultdict(list)
        for _ in range(E):
            u, v = map(int, sys.stdin.readline().split())
            graph[u].append(v)
            graph[v].append(u)
        
        print(bfs(v=V, graph=graph))
main()
############################# BFS 풀이 #################################

############################# DFS 풀이 #################################
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
def main():
    K = int(sys.stdin.readline().strip())
    def dfs(node, color, graph, colors):
        colors[node] = color
        for next_node in graph[node]:
            if colors[next_node] == -1:
                if not dfs(next_node, 1 - color, graph, colors):
                    return False
            if colors[next_node] == color:
                return False
        return True

    for _ in range(K):
        V, E = map(int, sys.stdin.readline().split())
        graph = defaultdict(list)
        for _ in range(E):
            u, v = map(int, sys.stdin.readline().split())
            graph[u].append(v)
            graph[v].append(u)
        colors = [-1] * (V + 1) # -1: 미방문, 0과 1: 두 개의 그룹
        bipartite = True
        for start in range(1, V + 1):
            if colors[start] == -1:
                if not dfs(start, 0, graph, colors):
                    bipartite = False
                    break
        print("YES" if bipartite else "NO")
main()      
############################# DFS 풀이 #################################