# 백준 5585. 거스름돈
# https://www.acmicpc.net/problem/5585
import sys
charge = 1000 - int(sys.stdin.readline().strip())
def sol(charge):
    cnt = 0
    
    for coin in [500, 100, 50, 10, 5, 1]:
        cnt += charge // coin
        charge %= coin
    print(cnt)
sol(charge=charge)