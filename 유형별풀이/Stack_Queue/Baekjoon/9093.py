# 9093 (단어 뒤집기)
# https://www.acmicpc.net/problem/9093

################### 스택을 활용한 풀이 ######################
import sys
from collections import deque
T = int(sys.stdin.readline().strip())

for _ in range(T):
    sentences = sys.stdin.readline().strip()
    sentences += ' '
    
    stack = deque()
    
    for j in sentences:
        if j!= " ":
            stack.append(j)
        else:
            while stack:
                print(stack.pop(),end='')
            print(' ',end='')
    print()
################### 스택을 활용한 풀이 ######################

################## 뒤집기 풀이 #####################
# import sys

# T = int(sys.stdin.readline().strip())

# for _ in range(T):
#     sentences = sys.stdin.readline().split()
    
#     for i in sentences:
#         print(i[::-1],end=' ')
#     print()
    
################## 뒤집기 풀이 #####################
    