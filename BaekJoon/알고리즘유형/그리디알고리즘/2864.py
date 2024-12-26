# 백준 2864. 5와 6의 차이
# https://www.acmicpc.net/problem/2864
import sys
A, B = sys.stdin.readline().split()
print(int(A.replace('6', '5')) + int(B.replace('6', '5')), int(A.replace('5', '6')) + int(B.replace('5', '6')))