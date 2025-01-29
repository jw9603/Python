# 백준 1874. 스택 수열
# https://www.acmicpc.net/problem/1874
import sys
n = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(n)]

def sol(nums):
    stack = []
    result = []
    start = 1
    flag = True
    
    for num in nums:
        
        while start <= num:
            stack.append(start)
            start += 1
            result.append('+')
            
        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            flag = False
    return '\n'.join(result) if flag else 'NO'
print(sol(nums=nums))
    