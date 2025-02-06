###################### 완전 탐색: O(T * 3^N)#######################
# import sys
# T = int(sys.stdin.readline().strip())
# def sol(n):
#     # 1. base case
#     if n == 0:
#         return 1
#     if n < 0:
#         return 0
    
#     # 2. 재귀 호출
#     return sol(n - 1) + sol(n - 2) + sol(n - 3)

        
# for _ in range(T):
#     n = int(sys.stdin.readline().strip())
#     print(sol(n=n))
# ###################### 완전 탐색 #######################

# ###################### Top-Down #######################
# import sys
# sys.setrecursionlimit(10**6)
# T = int(sys.stdin.readline().strip())
# def sol(n, memo):
#     # 1. base case
#     if n == 0:
#         return 1
#     if n < 0:
#         return 0
#     if n in memo:
#         return memo[n]
    
#     memo[n] = sol(n - 1, memo) + sol(n - 2, memo) + sol(n - 3, memo)
#     return memo[n]
# for _ in range(T):
#     n = int(sys.stdin.readline().strip())
#     memo = {}
#     print(sol(n=n, memo=memo))
###################### Top-Down #######################

###################### Bottom-UP #######################
import sys
T = int(sys.stdin.readline().strip())
def sol(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    tab = [0] * (n + 1)
    tab[1], tab[2], tab[3] = 1, 2, 4
    for i in range(4, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2] + tab[i - 3]
    return tab[n]
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    print(sol(n=n))
###################### Bottom-UP #######################