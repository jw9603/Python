# 백준 18870. 좌표 압축
# https://www.acmicpc.net/problem/18870
import sys
N = int(sys.stdin.readline().strip())
x_list = list(map(int, sys.stdin.readline().split()))
def sol(x_list):
    a = sorted(list(set(x_list)))
    cnt = {a[i]:i for i in range(len(a))}
    
    return ' '.join(str(cnt[i]) for i in x_list)
print(sol(x_list=x_list))