# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/

class Solution(object):
    
    ################# 1. Stack #################
    def dailyTemperatures(self,temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)
        stack = []
        
        for day,temp in enumerate(temperatures):
            
            while stack and stack[-1][1] < temp:
                prev_day, _ = stack.pop()
                ans[prev_day] = day - prev_day
            
            stack.append((day,temp))
        
        return ans
    ################# 1. Stack #################
    
    ##################### 2. Brute Force -> Time Limit Exceeded #####################
    # def dailyTemperatures(self,temperatures):
    #     """
    #     :type temperatures: List[int]
    #     :rtype: List[int]
    #     """
    #     n = len(temperatures)
    #     ans = [0] * n
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             if temperatures[j] > temperatures[i]:
    #                 ans[i] = j - i
    #                 break
    #     return ans
    ##################### 2. Brute Force -> Time Limit Exceeded #####################    
    
if __name__ == '__main__':
    
    a = Solution()
    
    print(f"Example 1: {a.dailyTemperatures([73,74,75,71,69,72,76,73])}")
    print(f"Example 2: {a.dailyTemperatures([30,40,50,60])}")
    print(f"Example 3: {a.dailyTemperatures([30,60,90])}")