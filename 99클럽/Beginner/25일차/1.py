from collections import defaultdict
from collections import deque

######################## Union-Find #################################
class Solution(object): # O(N+E)
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        # N : node
        # E : edge

        # initialize parent
        parent = list(range(n)) # O(N)
        
        # find root (path compression algorithm)
        def find(node):         
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
    
        for h,t in edges: # O(E * α(N))
            parent[find(h)] = find(t)

       
        return find(source) == find(destination) # O(α(N))
        

######################## Union-Find #################################

################### DFS - 1 (using Stack) ######################
class Solution_dfs1: # O(N+E)
    def validPath(self,n,edges,source,destination):
        
        graph = defaultdict(list)
        
        # 그래프를 인접 리스트 형태로 변환
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # 이미 방문한 노드들을 저장하는 배열    
        visited = [False] * n 
        
        # stack: 방문이 필요한 노도들을 저장하는 배열
        stack = [source]
        
        while stack:
            
            node = stack.pop()
            
            if node == destination:
                return True
            
            # 현재 노드를 방문했음을 기록
            if not visited[node]:
                visited[node] = True
                
                # 인접한 노드들을 스택에 추가
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
                        
        return False
################### DFS - 1 (using Stack) ######################


################### DFS - 2 (using recursive function) ######################
class Solution_dfs2: # O(N+E)
    def validPath(self,n,edges,source,destination):
        
        graph = defaultdict(list)
        
        # 그래프를 인접 리스트 형태로 변환
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # 이미 방문한 노드들을 저장하는 배열    
        visited = [False] * n 
        
        def dfs(node):
            
            if node == destination:
                return True
            visited[node] = True
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
            
            return False
        
        return dfs(source)
################### DFS - 2 (using recursive function) ######################

################### BFS (using Queue) ######################
class Solution_bfs: # O(N+E)
    def validPath(self,n,edges,source,destination):
        
        graph = defaultdict(list)
        
        # 그래프를 인접 리스트 형태로 변환
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # 이미 방문한 노드들을 저장하는 리스트
        visited = [False] * n
        
        # 방문이 필요한 노드들을 저장하는 큐
        queue = deque([source])
        
        while queue:
            node = queue.popleft()
            
            if node == destination:
                return True
            
            if not visited[node]:
                visited[node] = True
                
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
        
        return False
        
################### BFS (using Queue) ######################


# Test case
if __name__ == '__main__':

    a = Solution()
    b = Solution_dfs1()
    c = Solution_dfs2()
    d = Solution_bfs()
    
    # Test Case 1

    res_uf1 = a.validPath(3,[[0,1],[1,2],[2,0]],0,2)
    
    res_dfs1 = b.validPath(3,[[0,1],[1,2],[2,0]],0,2)
    
    res_dfs11 = c.validPath(3,[[0,1],[1,2],[2,0]],0,2)
    
    res_bfs1 = d.validPath(3,[[0,1],[1,2],[2,0]],0,2)
    
    print('Test case1 Result using union-find algorithm',res_uf1)
    print('Test case1 Result using DFS(stack) algorithm',res_dfs1)
    print('Test case1 Result using DFS(recursive) algorithm',res_dfs11)
    print('Test case1 Result using BFS algorithm',res_bfs1)
    
    
    # Test Case 2
    res_uf2 = a.validPath(6,[[0,1],[0,2],[3,5],[5,4],[4,3]],0,5)
    
    res_dfs2 = b.validPath(6,[[0,1],[0,2],[3,5],[5,4],[4,3]],0,5)
    
    res_dfs21 = c.validPath(6,[[0,1],[0,2],[3,5],[5,4],[4,3]],0,5)
    
    res_bfs2 = d.validPath(6,[[0,1],[0,2],[3,5],[5,4],[4,3]],0,5)
    
    print('Test case1 Result using union-find algorithm',res_uf2)
    print('Test case1 Result using DFS(stack) algorithm',res_dfs2)
    print('Test case1 Result using DFS(recursive) algorithm',res_dfs21)
    print('Test case1 Result using BFS algorithm',res_bfs2)