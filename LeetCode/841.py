# 841.  Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms/description/
from collections import deque
class Solution(object):
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
        
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        visited = [False] * len(rooms)
        
        def bfs(v):
            queue = deque()
            queue.append(v)
            visited[v] = True
            while queue:
                cur_v = queue.popleft()
                for next_v in rooms[cur_v]:
                    if not visited[next_v]:
                        queue.append(next_v)
                        visited[next_v] = True
                
        bfs(0)
        
        return all(visited)
if __name__ == '__main__':
    
    a = Solution()
    
    print(a.canVisitAllRooms([[1],[2],[3],[]]))
    print(a.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))