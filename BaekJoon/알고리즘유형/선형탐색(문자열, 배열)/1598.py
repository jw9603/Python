# 백준 1598. 꼬리를 무는 숫자 나열
# https://www.acmicpc.net/problem/1598
import sys
a, b = map(int, sys.stdin.readline().split())
print(abs((a-1) // 4 - (b - 1) // 4) + abs((a - 1) % 4 - (b - 1) % 4))