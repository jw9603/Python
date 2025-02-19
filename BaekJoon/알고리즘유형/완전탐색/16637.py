# 백준 16637. 괄호 추가하기
# https://www.acmicpc.net/problem/16637 
import sys

def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    
def dfs(idx, current_value):
    '''
    idx: operation의 인덱스
    current_value: 현재까지의 합
    '''
    global max_result
    
    # 1. base case:
    if idx >= len(operations):
        max_result = max(max_result, current_value)
        return
    
    # 2. 괄호를 넣지 않고 왼쪽에서 오른쪽부터 더하는 경우
    next_value = calculate(current_value, operations[idx], numbers[idx + 1])
    dfs(idx + 1, next_value)
    
    # 3. 괄호 추가
    if idx + 1 < len(operations):
        bracket_value = calculate(numbers[idx + 1], operations[idx + 1], numbers[idx + 2])
        next_value_with_bracket = calculate(current_value, operations[idx], bracket_value)
        dfs(idx + 2, next_value_with_bracket)
    

N = int(sys.stdin.readline().strip())
expression = sys.stdin.readline().strip()
numbers, operations = [], []
for e in expression:
    if e.isdigit():
        numbers.append(int(e))
    else:
        operations.append(e)
        
max_result = -float('inf')

dfs(0, numbers[0])
print(max_result)


    