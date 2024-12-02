# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/description/

from heapq import heappush, heappop
from collections import defaultdict
class Solution(object):
    def networkDelayTime(self, times, n, k):
        
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[2],time[1]))
        
        costs = {}
        pq = []
        heappush(pq, (0, k))
        
        while pq:
            cur_cost, cur_node = heappop(pq)
            if cur_node not in costs:
                costs[cur_node] = cur_cost
                for cost, next_node in graph[cur_node]:
                    next_cost = cost + cur_cost
                    heappush(pq, (next_cost, next_node))
                    
        for i in range(1, n + 1):
            if i not in costs:
                return -1
        return max(costs.values())