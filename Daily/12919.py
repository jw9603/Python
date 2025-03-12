# 백준 12919. A와 B 2
# https://www.acmicpc.net/problem/12919

# 첫 번째 풀이, 시간 초과: O(2^(len(T)- len(S))
import sys

def dfs(curr):
    global T
    # 1. base case
    if len(curr) == len(T):
        return 1 if curr == T else 0

    if len(curr) > len(T):
        return 0

    # 2. 재귀 호출 및 데이터 통합
    return dfs(curr + 'A') or dfs((curr + 'B')[::-1])

def main():
    global T
    S = sys.stdin.readline().strip()
    T = sys.stdin.readline().strip()

    print(dfs(curr=S))

if __name__ == '__main__':
    main()

# 두 번째 풀이, 시간 복잡도: O(len(T))
import sys

def dfs(T):
    global S
    # 1. base case: T와 S가 같아지면 성공
    if T == S:
        return 1
    
    # 2. base case: T가 S보다 짧아지면 실패
    if len(T) < len(S):
        return 0
    
    # 재귀 호출: 마지막 문자가 'A'이면 'A'를 제거
    if T[-1] == 'A':
        if dfs(T[:-1]):
            return 1
    
    # 재귀 호출: 맨압 문자가 'B'이면 'B'를 제거하고 뒤집기
    if T[0] == 'B':
        if dfs(T[1:][::-1]):
            return 1

    return 0

def main():
    global S
    S = sys.stdin.readline().strip()
    T = sys.stdin.readline().strip()

    print(dfs(T=T))

if __name__ == '__main__':
    main()