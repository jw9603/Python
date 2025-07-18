# 백준 1920. 수 찾기
# https://www.acmicpc.net/problem/1920
################################## 문제 이해 ##################################
# N개의 정수 A[1], A[2],..., A[N]이 주어졌을 때, 이 안에 X라는 정수가 존재하는지 알아내라.

# 입력
# 첫째 줄에 자연수 N이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2],..., A[N]이 주어진다.
# 다음 줄에는 M이 주어진다. 다음 줄에는 M개의 수들이 주어지는데,
# 이 수들이 A안에 존재하는 지 알아내면 된다.

# 출력: M개의 줄에 답을 출력, 존재하면 1, 존재하지 않으면 0

# 알고리즘
# 이 문제는 여러 방법으로 풀 수 있다.
# 찾기 때문에, 이진 탐색, Hash, 순차 탐색
# N의 범위가 1이상 10^5이므로 순차 탐색도 가능하다.
################################## 문제 이해 ##################################
# 1. 집합과 맵
def sol(A, nums):
    return [1 if num in A else 0 for num in nums]

def main():
    N = int(input().strip())
    A = set(map(int, input().split()))
    M = int(input().strip())
    nums = list(map(int, input().split()))

    print(*sol(A, nums), sep='\n')

if __name__ == '__main__':
    main()

# 2. 이진 탐색
from bisect import *
def sol(A, nums):
    A.sort()
    result = []

    for num in nums:
        idx = bisect_left(A, num)
        if idx < len(A) and A[idx] == num:
            result.append(1)
        else:
            result.append(0)
    
    return result
    
def main():
    N = int(input().strip())
    A = list(map(int, input().split()))
    M = int(input().strip())
    nums = list(map(int, input().split()))

    print(*sol(A, nums), sep='\n')

if __name__ == '__main__':
    main()