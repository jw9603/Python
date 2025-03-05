# LeetCode77. Combinations
# https://leetcode.com/problems/combinations/description/
# https://leetcode.com/problems/combinations/submissions/1563725894
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(start, curr):
            # 1. base case
            if len(curr) == k:
                ans.append(curr[:])
                return

            for num in range(start, n + 1):
                curr.append(num)
                dfs(num + 1, curr)
                curr.pop()
        dfs(1, [])
        return ans

if __name__ == '__main__':
    n1, k1 = 4, 2
    n2, k2 = 1, 1
    
    sol = Solution()
    print(f"Result1: {sol.combine(n=n1, k=k1)}")
    print(f"Result2: {sol.combine(n=n2, k=k2)}")