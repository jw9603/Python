# 백준 2164. 카드2
# https://www.acmicpc.net/problem/2164
################################### 문제 이해 ###################################
# 1부터 N(5)까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 밑에 있다.
# 1. 제일 위의 카드를 바닥에 버린다. -> [1, 2, 3, 4, 5], 1을 제거 (popleft)
# 2. [2, 3, 4, 5] -> a = popleft(), [3, 4, 5].append(a) = [3, 4, 5, 2]

# 이 두 가지 스텝을 반복, 1개가 남을 때 까지
################################### 문제 이해 ###################################
from collections import deque
def sol(N):
    nums = deque([i for i in range(1, N + 1)])

    while len(nums) > 1:
        nums.popleft()
        a = nums.popleft()
        nums.append(a)
    
    return nums

def main():
    N = int(input().strip())

    print(*sol(N))

if __name__ == '__main__':
    main()
