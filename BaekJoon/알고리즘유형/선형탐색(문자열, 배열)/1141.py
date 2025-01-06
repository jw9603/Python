# 백준 1141. 접두사
# https://www.acmicpc.net/problem/1141
import sys
N = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(N)]
def sol(N, words):
    words.sort(key=len)
    cnt = 0
    for i in range(N):
        flag = False
        for j in range(i + 1, N):
            if words[i] == words[j][:len(words[i])]:
                flag = True
                break
        if not flag:
            cnt += 1
    return cnt
print(sol(N=N, words=words))
    