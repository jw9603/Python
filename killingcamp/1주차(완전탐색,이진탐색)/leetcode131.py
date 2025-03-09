# LeetCode 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/description/
# https://leetcode.com/problems/palindrome-partitioning/submissions/1567782962
class Solution(object):
    def is_palindrome(self, word):
        return word == word[::-1]
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        def dfs(start, curr):
            # 1. base case
            if start == len(s):
                ans.append(curr[:])
                return

            for end in range(start + 1, len(s) + 1):
                if self.is_palindrome(s[start:end]):
                    curr.append(s[start:end])
                    dfs(end, curr)
                    curr.pop()
        dfs(0, [])
        return ans

if __name__ == '__main__':
    s1, s2 = "aab", "a"
    sol = Solution()
    print(f"Result1: {sol.partition(s=s1)}")
    print(f"Result2: {sol.partition(s=s2)}")