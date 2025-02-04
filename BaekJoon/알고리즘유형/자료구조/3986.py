# 백준 3986. 좋은 단어
# https://www.acmicpc.net/problem/3986
import sys
N = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(N)]
def sol(word):
    stack = []
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0

print(sum(sol(word) for word in words))