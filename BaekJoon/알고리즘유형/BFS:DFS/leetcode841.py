# LeetCode 841. Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms/
from collections import deque
class Solution(object):
    ################## DFS ##################
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False] * len(rooms)

        def dfs(v):
            visited[v] = True
            for next_v in rooms[v]:
                if not visited[next_v]:
                    dfs(next_v)
        dfs(0)

        return all(visited)
    ################## DFS ##################
    
    ################## BFS ######################
    
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False] * len(rooms)
        
        def bfs(v):
            q = deque()
            q.append(v)
            visited[v] = True
            while q:
                cur_v = q.popleft()
                for next_v in rooms[cur_v]:
                    if not visited[next_v]:
                        visited[next_v] = True
                        q.append(next_v)
        bfs(0)
        return all(visited)
    ################## BFS ######################
                        
            