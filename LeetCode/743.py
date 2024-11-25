# 743. NetWork Delay Time
# https://leetcode.com/problems/network-delay-time/description/
from heapq import heappush, heappop
from collections import defaultdict
class Solution(object):
    def networkDelayTime(self, times, n, k):
        # https://leetcode.com/problems/network-delay-time/submissions/1462136700
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        
        graph = defaultdict(list)
        
        for time in times:
            graph[time[0]].append((time[2], time[1]))
            
        pq = []
        heappush(pq, (0, k))
        costs = {}
        
        while pq:
            
            cur_cost, cur_node = heappop(pq)
            if cur_node not in costs:
                costs[cur_node] = cur_cost
                for cost, next_node in graph[cur_node]:
                    next_cost = cur_cost + cost
                    heappush(pq,(next_cost, next_node))
        
        for i in range(1, n + 1):
            if i not in costs:
                return - 1
            
        return max(costs.values())
    
if __name__ == '__main__':
    
    a = Solution()
    
    print(a.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
    print(a.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
    print(a.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))