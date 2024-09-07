# 2839 - 설탕 배달
# https://www.acmicpc.net/problem/2839


# 3키로와 5키로 봉지가 있음

######################## greedy ################
import sys

N = int(sys.stdin.readline().strip())

def sugar_delivery_greedy(N):
    cnt = 0
    
    while N >= 0:
        
        if N % 5 == 0:
            cnt += N // 5
            return cnt
        else:
            N -= 3
            cnt += 1
            
    return -1

print(sugar_delivery_greedy(N))
######################## greedy ################

    
#################### Dynamic Programming ##########################
import sys

def sugar_delivery_dp(N):
    INF = 5001  # 큰 값으로 설정 (최대 5000kg까지 가능하므로 5001 이상이면 불가능한 경우)
    dp = [INF] * (N + 1)
    
    dp[0] = 0  # 0kg은 0개의 봉지가 필요함
    
    # 동적 프로그래밍으로 dp 테이블 채우기
    for i in range(3, N + 1):
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + 1)
        if i >= 5:
            dp[i] = min(dp[i], dp[i - 5] + 1)
    
    # dp[N]이 여전히 INF이면 Nkg을 만들 수 없다는 의미
    return dp[N] if dp[N] != INF else -1

# 입력 처리
N = int(sys.stdin.readline().strip())

# 결과 출력
print(sugar_delivery_dp(N))
#################### Dynamic Programming ##########################
