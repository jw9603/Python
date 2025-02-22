# leetcode 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

########################## 완전 탐색 풀이 ###########################
# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         # 1. base case
#         if n == 0:
#             return 1

#         # 2. 재귀 호출
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)
########################## 완전 탐색 풀이 ###########################
########################## Top-Down 풀이 ###########################
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def dp(n):
            # 1. base case
            if n == 0 or n == 1:
                return 1
            
            if n in memo:
                return memo[n]
            
            # 2. 재귀호출
            memo[n] = dp(n - 1) + dp(n - 2)
            
            return memo[n]
        return dp(n)
########################## Top-Down 풀이 ###########################
########################## Bottom-Up 풀이 ###########################
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        tab = [1] * (n + 1)
        for i in range(2, n + 1):
            tab[n] = tab[n - 1] + tab[n - 2]
        return tab[n]
########################## Bottom-Up 풀이 ###########################

if __name__ == '__main__':
    a = Solution()
    print(a.climbStairs(2))