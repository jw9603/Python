# 백준 14888. 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
############################### 문제 이해 ###############################
# N개의 수로 이루어진 수열이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N - 1개의 연산자가
# 주어진다. 연산자는 +, -, *, /으로만 이루어져 있다.

# 우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다.
# 이때, 주어진 수의 순서를 바꾸면 안 된다.
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행, 나눗셈은 정수 나눗셈으로 몫만 취한다.

# N개의 수와 N - 1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구해라

# 입력
# 첫째 줄에 수의 개수 N이 주어진다. 둘째 줄에는 A1,..., A_N이 주어진다.
# 차례대로 덧셈의 개수, 뺄셈의 개수, 곱셈의 개수, 나눗셈의 개수가 주어진다.

# 출력
# 첫 줄에 최댓값, 둘째 줄에 최솟값을 출력
############################### 문제 이해 ###############################
# 1. BackTracking
# def dfs(index, current_result, plus, minus, mul, div):
#     global N, A, operators_cnt, max_result, min_result

#     if index == N:
#         max_result = max(max_result, current_result)
#         min_result = min(min_result, current_result)
#         return
    
#     if plus > 0:
#         dfs(index + 1, current_result + A[index], plus - 1, minus, mul, div)
    
#     if minus > 0:
#         dfs(index + 1, current_result - A[index], plus, minus - 1, mul, div)
    
#     if mul > 0:
#         dfs(index + 1, current_result * A[index], plus, minus, mul - 1, div)
    
#     if div > 0:
#         if current_result < 0:
#             dfs(index + 1, -(-current_result // A[index]), plus, minus, mul, div - 1)
#         else:
#             dfs(index + 1, current_result // A[index], plus, minus, mul, div - 1)

# def main():
#     global N, A, operators_cnt, max_result, min_result
#     N = int(input().strip())
#     A = list(map(int, input().split()))
#     operators_cnt = list(map(int, input().split()))
#     max_result, min_result = -float('inf'), float('inf')

#     dfs(1, A[0], *operators_cnt)

#     print(max_result, min_result, sep='\n')

# if __name__ == '__main__':
#     main()

# 2. itertools
from itertools import permutations
def sol(N, A, operators_cnt):
    max_result, min_result = -float('inf'), float('inf')
    operators = []
    for i, cnt in enumerate(operators_cnt):
        operators.extend(['+', '-', '*', '/'][i] * cnt)
    
    for perm in permutations(operators):

        result = A[0]

        for i in range(1, N):
            if perm[i - 1] == '+':
                result += A[i]
            elif perm[i - 1] == '-':
                result -= A[i]
            elif perm[i - 1] == '*':
                result *= A[i]
            else:
                if result < 0:
                    result = -(-result // A[i])
                else:
                    result //= A[i]
        
        max_result = max(max_result, result)
        min_result = min(min_result, result)
    
    return max_result, min_result

def main():
    N = int(input().strip())
    A = list(map(int, input().split()))
    operators_cnt = list(map(int, input().split()))

    print(*sol(N, A, operators_cnt), sep='\n')

if __name__ == '__main__':
    main()