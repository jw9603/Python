# 백준 2798. 블랙잭
# https://www.acmicpc.net/problem/2798
################################### 문제 이해 ###################################
# 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다.
# 그런 후에 숫자 M을 외친다.
# 플레이어는 N장의 카드 중에서 3장의 카드를 골라야 한다.
# 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

# 입력:
# 첫째 줄에 카드의 개수 N과 M이 주어진다.
# 둘째 줄에는 카드에 쓰여있는 수가 주어진다.
# 출력: M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

# 알고리즘
# 3 <= N <= 100, 10 <= M <= 3 * 10^5
# 3중 반복문을 사용해서 푸는 완전 탐색이 있고, 조합 알고리즘을 사용해서 풀수도 있다.
################################### 문제 이해 ###################################
from itertools import combinations
def sol(M, nums):
    max_sum = 0

    for comb in combinations(nums, 3):
        temp_sum = sum(comb)

        if max_sum < temp_sum <= M:
            max_sum = temp_sum
        
    return max_sum

def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    print(sol(M, nums))

if __name__ == '__main__':
    main()

# 반복문 풀이
def sol(N, M, nums):
    res = 0

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                val = nums[i] + nums[j] + nums[k]
                if val > M:
                    continue
                else:
                    res = max(res, val)
    return res

def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    print(sol(N, M, nums))

if __name__ == '__main__':
    main()