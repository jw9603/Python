# 백준 2839. 설탕 배달
# https://www.acmicpc.net/problem/2839
############################ 문제 이해 ############################
# 사탕가게에 N킬로그램을 배달해야 한다.
# 봉지는 3kg, 5kg 봉지가 있다.
# 최대한 적은 봉지를 들고 가려고 한다.
############################ 문제 이해 ############################
########################### 그리디 ###########################
def sol(N):
    cnt = 0

    while N >= 0:

        if N % 5 == 0:
            cnt += N // 5
            return cnt
        else:
            N -= 3
            cnt += 1
    return -1
    
def main():
    N = int(input().strip())
    print(sol(N))

if __name__ == '__main__':
    main()
########################## 그리디 ###########################
########################## 완탐 (RecursionError)############################
def sol(N, cnt):
    if N == 0:
        return cnt
    
    if N < 0:
        return float('inf')
    
    res_3 = sol(N - 3, cnt + 1)
    res_5 = sol(N - 5, cnt + 1)

    return min(res_3, res_5)
 
def main():
    N = int(input().strip())
    result = sol(N, 0)
    print(result if result != float('inf') else -1)

if __name__ == '__main__':
    main()
########################### 완탐 (RecursionError)############################

########################### Top-Down ###########################
def sol(N):
    global memo

    if N < 0:
        return float('inf')

    if N == 0:
        return 0
    
    if N in memo:
        return memo[N]
    
    res = min(sol(N - 3), sol(N - 5)) + 1
    memo[N] = res

    return memo[N]
         
def main():
    global memo
    N = int(input().strip())
    memo = {}
    result = sol(N)
    print(result if result != float('inf') else -1)

if __name__ == '__main__':
    main()
########################### Top-Down ###########################

########################### Bottom-Up ###########################
def sol(N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for i in range(3, N + 1):
        if i >= 3 and dp[i - 3] != float('inf'):
            dp[i] = min(dp[i], dp[i - 3] + 1)
        if i >= 5 and dp[i - 5] != float('inf'):
            dp[i] = min(dp[i], dp[i - 5] + 1)

    return dp[N] if dp[N] != float('inf') else -1

def main():
    N = int(input().strip())
    print(sol(N))

if __name__ == '__main__':
    main()
########################### Bottom-Up ###########################
