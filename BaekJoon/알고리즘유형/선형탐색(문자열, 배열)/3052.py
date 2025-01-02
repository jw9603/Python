# 백준 3052. 나머지
# https://www.acmicpc.net/problem/3052
import sys
nums = [int(sys.stdin.readline().strip()) for _ in range(10)]
def sol(nums):
    result = set()
    for i in nums:
        result.add(i % 42)
    return len(result)
print(sol(nums=nums))