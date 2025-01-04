# 백준 1515. 수 이어 쓰기
# https://www.acmicpc.net/problem/1515
import sys
s = sys.stdin.readline().strip()
def sol(s):
    N = 0
    while True:
        N += 1
        num = str(N)
        while len(num) > 0 and len(s) > 0:
            if num[0] == s[0]:
                s = s[1:]
            num = num[1:]
        if s == '':
            print(N)
            break
sol(s=s)