# 1935. 후위 표기식2
# https://www.acmicpc.net/problem/1935
import sys
N = int(sys.stdin.readline().strip())
equation = sys.stdin.readline().strip()
stack = []
num_list = [0] * N
for i in range(N):
    num_list[i] = int(sys.stdin.readline().strip())
    
for i in equation:
    if 'A' <= i <= 'Z':
        stack.append(num_list[ord(i) - ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()
        
        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)
print(f"{stack[0]:.2f}")        
        
        