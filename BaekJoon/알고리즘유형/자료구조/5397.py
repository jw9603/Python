# 백준 5397. 키로거
# https://www.acmicpc.net/problem/5397
import sys
T = int(sys.stdin.readline().strip())
def find_word(s):
    left_stack, right_stack = [], []
    
    for char in s:
        if char == '-':
            if left_stack:
                left_stack.pop()
        elif char == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(char)
    return ''.join(left_stack) + ''.join(reversed(right_stack))
            
            
for _ in range(T):
    s = sys.stdin.readline().strip()
    print(find_word(s=s))
    