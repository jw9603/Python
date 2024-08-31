# https://leetcode.com/problems/n-th-tribonacci-number/description/
# 1137. N-th Tribonacci Number
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n== 1 or n== 2:
            return 1

        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        return dp[n]
    
if __name__ == '__main__':
    
    
    a = Solution()
    res1 = a.tribonacci(4)
    res2 = a.tribonacci(25)
    
    print(f"Test Case1 Result: {res1}")
    print(f"Test Case2 Result: {res2}")