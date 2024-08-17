# BFS

from collections import deque

def bfs(graph, start):
    visited = []
    need_visit = deque([start])
    
    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    
    return visited

if __name__ == '__main__':
    
    graph = {}

    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D']
    graph['C'] = ['A', 'G', 'H', 'I']
    graph['D'] = ['B', 'E', 'F']
    graph['E'] = ['D']
    graph['F'] = ['D']
    graph['G'] = ['C']
    graph['H'] = ['C']
    graph['I'] = ['C', 'J']
    graph['J'] = ['I']
    
    print(f"BFS 방문 순서: {bfs(graph=graph,start='A')}")