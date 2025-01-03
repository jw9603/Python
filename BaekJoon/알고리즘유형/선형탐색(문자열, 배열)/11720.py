# 백준 11720. 숫자의 합
# https://www.acmicpc.net/problem/11720
import sys
N = int(sys.stdin.readline().strip())
num = sys.stdin.readline().strip()
print(sum(map(int, num)))