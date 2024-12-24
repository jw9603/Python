# 백준 1744. 수 묵기
# https://www.acmicpc.net/problem/1744

# 양수는 큰 양수끼리
# 음수는 작은 음수끼리(절댓값이 큰 음수끼리)
# 음수가 1개 남았을 때 0이 있다면 0과, 0이 없다면 그냥 더하기
import sys
N = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(N)]

def sol(N, nums):
    positive = []
    negative = []
    zeros = 0
    ones = 0
    for num in nums:
        if num > 1:
            positive.append(num)
        elif num == 1:
            ones += 1
        elif num == 0:
            zeros += 1
        else:
            negative.append(num)
    positive.sort(reverse=True)
    negative.sort()
    
    total_sum = 0
    
    for i in range(0, len(positive) - 1, 2):
        total_sum += positive[i] * positive[i + 1]
    if len(positive) % 2 == 1:
        total_sum += positive[-1]
        
    for i in range(0, len(negative) - 1, 2):
        total_sum += negative[i] * negative[i + 1]
    if len(negative) % 2 == 1:
        if zeros == 0:
            total_sum += negative[-1]
    
    total_sum += ones
    
    return total_sum
print(sol(N=N, nums=nums))