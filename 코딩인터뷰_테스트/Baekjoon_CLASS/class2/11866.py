# 백준 11866. 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866
#################################### 문제 이해 ####################################
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K가 주어진다.
# 이제 순서대로 K번째 사람을 제거한다.
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
# 이 과정은 N 명의 사람이 모두 제거될 때까지 계속된다.

# 입력: N과 K가 빈 칸을 사이에 두고 주어진다.
# 출력: 요세푸스 순열을 출력
#################################### 문제 이해 ####################################
from collections import deque
def sol(n, k):
    nums = deque([i for i in range(1, n + 1)])
    result = []

    while len(nums) >= 1:
        nums.rotate(-(k - 1))
        result.append(str(nums.popleft()))

    return '<' + ', '.join(result) + '>'
def main():
    N, K = map(int, input().split())
    print(sol(N, K))

if __name__ == '__main__':
    main()