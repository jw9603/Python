# LeetCode 60. Permutation Sequence
# https://leetcode.com/problems/permutation-sequence/description/
# https://leetcode.com/problems/permutation-sequence/submissions/1567802432
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = []
        visited = [False] * (n + 1)
        self.count = 0
        def dfs(curr):
            # 1. base case
            if len(curr) == n:
                self.count += 1
                if self.count == k:
                    ans.append(''.join(map(str, curr)))
                    return
                return
            
            for num in range(1, n + 1):
                if not visited[num]:
                    visited[num] = True
                    curr.append(num)
                    dfs(curr)
                    if ans:
                        return
                    curr.pop()
                    visited[num] = False
        dfs([])
        return ans[0]
    
if __name__ == '__main__':
    n1, k1 = 3, 3
    n2, k2 = 4, 9
    n3, k3 = 3, 1
    sol = Solution()
    print(f"Result1: {sol.getPermutation(n=n1, k=k1)}")
    print(f"Result2: {sol.getPermutation(n=n2, k=k2)}")
    print(f"Result3: {sol.getPermutation(n=n3, k=k3)}")