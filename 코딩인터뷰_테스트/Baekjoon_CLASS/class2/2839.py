# 백준 2839. 설탕 배달
# https://www.acmicpc.net/problem/2839
############################# 문제 이해 #############################
# 상근이는 설탕공장에서 설타을 배달하고 있다.
# 상근이는 사탕가게에서 설탕을 정확하게 N kg을 배달해야 한다.
# 봉지는 3킬로그램과 5킬로그램 봉지가 있다.
# 상근이는 최대한 적은 봉지를 들고 가려고 한다.

# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 구해라

# 입력 3 <= N <= 5000
# 출력: 봉지의 최소 개수

# 알고리즘
# 무조건 N을 꽉채워야 한다.
# 그리고 봉지는 두 종류 5, 3이 있다.
# 그러면 5로 최대한 많이 담으면 된다. -> Greedy
############################# 문제 이해 #############################
# 1. Greedy Algorithm
def sol(N):
    cnt = 0

    while N >= 0:
        if N % 5 == 0:
            cnt += N // 5
            return cnt
        
        N -= 3
        cnt += 1
    else:
        return -1
    
def main():
    N = int(input().strip())
    print(sol(N))

if __name__ == '__main__':
    main()

# 2. DP - Top Down
import sys
sys.setrecursionlimit(10 ** 6)
def dp(n, memo):
    if n < 0:
        return float('inf')
    if n == 0:
        return 0
    if memo[n] != -1:
        return memo[n]
    memo[n] = min(dp(n - 3, memo), dp(n - 5, memo)) + 1
    
    return memo[n]

def main():
    N = int(input().strip())
    memo = [-1] * (N + 1)
    res = dp(N, memo)
    
    print(res if res != float('inf') else -1)

if __name__ == '__main__':
    main()

# 3. DP - Bottom-Up
def dp(n):
    tab = [float('inf')] * (n + 1)
    tab[0] = 0 # 0 kg을 만드는 데 필요한 봉지 수 = 0

    for i in range(3, n + 1):
        if i >= 3:
            tab[i] = min(tab[i], tab[i - 3] + 1)
        if i >= 5:
            tab[i] = min(tab[i], tab[i - 5] + 1)
    
    return tab[n] if tab[n] != float('inf') else -1

def main():
    N = int(input().strip())
    
    print(dp(N))

if __name__ == '__main__':
    main()