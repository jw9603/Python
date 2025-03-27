# LeetCode 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/

############################## 완전 탐색 ##############################
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        if n == 0:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
############################## 완전 탐색 ##############################

############################## Top-Down ##############################
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def dp(n):
            if n == 0 or n == 1:
                return 1
            
            if n in memo:
                return memo[n]
            
            memo[n] = dp(n - 1) + dp(n - 2)
            
            return memo[n]
        
        return dp(n)
############################## Top-Down ##############################

############################## Bottom-Up ##############################
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        tab = [0] * (n + 1)
        tab[0] = 1
        tab[1] = 1

        for i in range(3, n + 1):
            tab[i] = tab[i - 1] + tab[i - 2]
        return tab[n]
############################## Bottom-Up ##############################
    


if __name__ == '__main__':
    sol = Solution()
    n1, n2 = 2, 3
    print(f"Result1: {sol.climbStairs(n1)}")
    print(f"Result2: {sol.climbStairs(n2)}")