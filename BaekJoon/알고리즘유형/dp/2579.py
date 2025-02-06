# 백준 2579. 계단 오르기
# https://www.acmicpc.net/problem/2579
####################### 완전 탐색: O(2^N) ##########################
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
score = [int(sys.stdin.readline()) for _ in range(N)]

def brute_force(k, count):
    '''
    parameters:
    k: 현재 위치한 계단의 인덱스 (0 <= k <= N - 1)
    count: 연속으로 밟은 계단의 개수 (0: 직전 계단을 밟지 않고 현재 계단으로 온 경우, 1: 직전 계단을 밟고 현재 계단으로 온 경우)
    score: 계단 점수 리스트
    '''
    # Base Case: 첫 번째 계단
    if k == 0:
        return score[0]

    # Base Case: 두 번째 계단
    if k == 1:
        if count == 0:
            return score[0] + score[1]  # 1칸씩 이동한 경우
        else:
            return score[1]  # 2칸 건너뛴 경우

    # 연속 2칸 이동 후 도착한 경우
    if count == 1:
        return score[k] + brute_force(k - 2, 0)

    # 한 칸 이동 vs. 두 칸 이동 중 최대 점수 선택
    return score[k] + max(brute_force(k - 2, 0), brute_force(k - 1, 1))

print(brute_force(N-1, 0))  # 마지막 계단에서 시작
####################### 완전 탐색 ##########################

###################### Top-Down: O(N) ##########################
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
score = [int(sys.stdin.readline()) for _ in range(N)]
dp = [[0] * 2 for _ in range(N)]  # 2차원 DP 테이블

def stair(k, count):
    '''
    parameters:
    k: 현재 위치한 계단의 인덱스 0 <= k <= N - 1
    count: 연속으로 밟은 계단의 개수: 0은 직전 계단을 밟지 않고 현재 계단으로 온 것, 1은 직전 계단을 밟고 현재 계단으로 온 것
    score: 계단 점수
    dp: dp[k][count]는 k번째 계단에 count연속으로 도착했을 때의 최대 점수
    '''
    # Base Case: 첫 번째 계단
    if k == 0:
        dp[0][0] = dp[0][1] = score[0]
        return dp[k][count]

    # Base Case: 두 번째 계단
    if k == 1:
        dp[1][0] = score[0] + score[1]  # 1칸씩 이동한 경우
        dp[1][1] = score[1]  # 2칸 건너뛴 경우
        return dp[k][count]

    # 메모이제이션 (이미 계산된 값이면 반환)
    if dp[k][count]:
        return dp[k][count]
    
    # 연속 2칸 이동 후 도착한 경우
    if count == 1:
        dp[k][count] = score[k] + stair(k-2, 0)
        return dp[k][count]
    
    # 한 칸 이동 vs. 두 칸 이동 중 최대 점수 선택
    dp[k][count] = score[k] + max(stair(k-2, 0), stair(k-1, 1))
    return dp[k][count]

print(stair(N-1, 0))  # 마지막 계단에서 시작
###################### Top-Down ##########################

####################### Bottom -Up: O(N) #########################
import sys
n = int(sys.stdin.readline().strip())
scores = [int(sys.stdin.readline().strip()) for _ in range(n)]

def sol(n, scores):
    if n == 1:
        return scores[0]
    elif n == 2:
        return scores[0] + scores[1]
    tab = [0] * n
    tab[0] = scores[0]
    tab[1] = scores[0] + scores[1]
    tab[2] = max(scores[2] + scores[0], scores[2] + scores[1])
    
    for i in range(3, n):
        tab[i] = max(scores[i] + scores[i - 1] + tab[i - 3], scores[i] + tab[i - 2])
    return tab[-1]
print(sol(n=n, scores=scores))
####################### Bottom -Up #########################