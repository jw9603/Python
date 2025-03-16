# LeetCode 322. Coin Change
# https://leetcode.com/problems/coin-change/description/
# https://leetcode.com/problems/coin-change/submissions/1575654138
from collections import deque
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        
        queue = deque([(amount, 0)])
        visited = set([amount])

        while queue:
            cur_amount, cur_cnt = queue.popleft()

            for coin in coins:
                next_amount = cur_amount - coin
                if next_amount == 0:
                    return cur_cnt + 1
                
                if next_amount > 0 and next_amount not in visited:
                    queue.append((next_amount, cur_cnt + 1))
                    visited.add(next_amount)
        return -1
    
if __name__ == '__main__':
    coins1, coins2, coins3 = [1, 2, 5], [2], [1]
    amount1, amount2, amount3 = 11, 3, 0
    sol = Solution()
    print(f"Result1: {sol.coinChange(coins=coins1, amount=amount1)}")
    print(f"Result2: {sol.coinChange(coins=coins2, amount=amount2)}")
    print(f"Result3: {sol.coinChange(coins=coins3, amount=amount3)}")