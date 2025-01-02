# 백준 1267. 핸드폰 요금
import sys
N = int(sys.stdin.readline().strip()) # 통화의 개수
times = list(map(int, sys.stdin.readline().split()))
def sol(times):
    y, m = 0, 0
    for i in times:
        y += (i // 30 + 1) * 10
        m += (i // 60 + 1) * 15
    return y, m
y, m = sol(times=times)
if y == m:
    print(f"Y M {y}")
elif y > m:
    print(f"M {m}")
else:
    print(f"Y {y}")
