# 백준 1935. 후위 표기식2
# https://www.acmicpc.net/problem/1935
import sys
N = int(sys.stdin.readline().strip())
equation = sys.stdin.readline().strip()

def sol(equation, N):
    stack = []
    num_list = [0] * N
    for i in range(N):
        num_list[i] = int(sys.stdin.readline().strip())
    
    for char in equation:
        if char.isalpha():
            stack.append(num_list[ord(char) - ord('A')])
        else: # 연산자
            str2 = stack.pop()
            str1 = stack.pop()
            
            if char == '+':
                stack.append(str1 + str2)
            elif char == '-':
                stack.append(str1 - str2)
            elif char == '*':
                stack.append(str1 * str2)
            else:
                stack.append(str1 / str2)
    return stack[0]    
print(f"{sol(equation=equation, N=N):.2f}")
                
            
    