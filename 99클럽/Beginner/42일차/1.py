class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0
        min_price = 10 ** 4


        for price in prices:
            min_price = min(min_price,price)
            profit = price - min_price

            max_profit = max(profit, max_profit) 


        return max_profit   
    
    
if __name__ == '__main__':
    
    a = Solution()
    
    res1 = a.maxProfit([7,1,5,3,6,4])
    res2 = a.maxProfit([7,6,4,3,1])
    
    print(f"Test Case1 Result: {res1}")
    print(f"Test Case2 Result: {res2}")