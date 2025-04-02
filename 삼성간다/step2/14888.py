# 백준 14888. 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
###################################### 백트래킹 ######################################
def dfs(index, current_result, plus, minus, mul, div):
    global max_result, min_result, N, A

    if index == N:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return
    
    if plus > 0:
        dfs(index + 1, current_result + A[index], plus - 1, minus, mul, div)
    if minus > 0:
        dfs(index + 1, current_result - A[index], plus, minus - 1, mul, div)
    if mul > 0:
        dfs(index + 1, current_result * A[index], plus, minus, mul - 1, div)
    if div > 0:
        if current_result < 0:
            dfs(index + 1, -(-current_result // A[index]), plus, minus, mul, div - 1)
        else:
            dfs(index + 1, current_result // A[index], plus, minus, mul, div - 1)

def main():
    global N, A, operators_cnt, max_result, min_result
    N = int(input().strip())
    A = list(map(int, input().split()))
    operators_cnt = list(map(int, input().split())) # +, -, x, / 개수 리스트

    max_result, min_result = -float('inf'), float('inf')

    dfs(1, A[0], *operators_cnt)

    print(max_result, min_result, sep='\n')

if __name__ == '__main__':
    main()
###################################### 백트래킹 ######################################

###################################### itertools ######################################
from itertools import permutations
def solution(N, A, operators_cnt):
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
    operators_cnt = list(map(int, input().split())) # +, -, x, / 개수 리스트

    print(*solution(N, A, operators_cnt), sep='\n')

if __name__ == '__main__':
    main()
###################################### itertools ######################################