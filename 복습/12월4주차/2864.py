# 백준 2864. 5와 6의 차이
# https://www.acmicpc.net/problem/2864
import sys
a, b = sys.stdin.readline().split()
print(int(a.replace('6','5')) + int(b.replace('6', '5')), int(a.replace('5','6')) + int(b.replace('5', '6')))