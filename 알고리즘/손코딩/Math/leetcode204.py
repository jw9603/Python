# LeetCode 204. Count Prime
# https://leetcode.com/problems/count-primes/
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        에라토스테네스의 체
        """
        if n <= 2:
            return 0
        
        is_prime = [True] * (n + 1)
        is_prime[0:2] = [False, False]

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        
        return sum(is_prime[:n])

if __name__ == '__main__':
    a = Solution()
    print(a.countPrimes(n=10))
    print(a.countPrimes(n=2))