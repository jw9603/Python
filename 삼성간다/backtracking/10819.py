# 백준 10819. 차이를 최대로
# https://www.acmicpc.net/problem/10819
############################## 백 트래킹 ##############################
def calculate(N, arr):
    return sum(abs(arr[i] - arr[i + 1]) for i in range(N - 1))

def permute(N, A):
    max_val = -float('inf')
    used = [False] * N
    def backtrack(N, curr):
        nonlocal max_val

        # 1. base case
        if len(curr) == len(A):
            max_val = max(max_val, calculate(N, curr))
            return
        
        for i in range(N):
            if not used[i]:
                used[i] = True
                curr.append(A[i])
                backtrack(N, curr)
                curr.pop()
                used[i] = False

    backtrack(N, [])

    return max_val

def main():
    N = int(input().strip())
    A = list(map(int, input().split()))

    print(permute(N, A))

if __name__ == '__main__':
    main()
############################## 백 트래킹 ##############################

############################## itertools ##############################
from itertools import permutations

def sol(N, A):
    max_val = -float('inf')

    for perm in permutations(A):
        current_val = 0
        for i in range(N - 1):
            current_val += abs(perm[i] - perm[i + 1])

        max_val = max(max_val, current_val)
    
    return max_val

def main():
    N = int(input().strip())
    A = list(map(int, input().split()))

    print(sol(N, A))

if __name__ == '__main__':
    main()
############################## itertools ##############################