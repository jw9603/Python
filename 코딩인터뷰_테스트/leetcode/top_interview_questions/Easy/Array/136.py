# LeetCode 136. Single Number
# https://leetcode.com/problems/single-number/description/
from collections import Counter
class Solution(object):
    # 1. 해쉬 풀이: 시간 복잡도는 O(n), 공간복잡도 O(n)
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)

        for key in counter:
            if counter[key] == 1:
                return key
    # 2. 해쉬 풀이: 시간 복잡도는 O(n), 공간복잡도 O(1)
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        
        return result
        # 주어진 문제는 한 값만 빼고 다 두번씩 반복됨.
        # 그렇기 때문에 모든 값을 XOR을 하면, 짝이 있는 값들은 0이 되고, 한 번 등장한 값만 남는다.
        # XOR의 규칙
        # 1. a^a = 0
        # 2. a^0 = a
        # 3. x ^ y ^ x = y , 교환, 결합 법칙 모두 가능

        # 0 ^ 4 = 4
        # 4 ^ 1 = 100 ^ 001 = 101 = 5
        # 5 ^ 2 = 101 ^ 010 = 111 = 7
        # 7 ^ 1 = 111 ^ 001 = 110 = 6
        # 6 ^ 2 = 110 ^ 010 = 100 = 4

        # 이걸 더 쉽게 XOR을 쓰는 이유로 말하면,
        # 4 ^ 1 ^ 2 ^ 1 ^ 2 = 4 ^ (1 ^ 1) ^ (2 ^ 2) = 4 ^ 0 ^ 0 = 4