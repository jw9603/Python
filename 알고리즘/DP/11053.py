# 백준 11053. 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
################################ 문제 이해 ################################
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열
#
################################ 문제 이해 ################################
def sol(N, A):
    dp = [1] * N

    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def main():
    N = int(input().strip())
    A = list(map(int, input().split()))

    print(sol(N, A))

if __name__ == '__main__':
    main()