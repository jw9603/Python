# 백준 20546. 기적의 매매법
# https://www.acmicpc.net/problem/20546
import sys
money = int(sys.stdin.readline().strip())
stocks = list(map(int, sys.stdin.readline().split()))

def junhyun():
    left_money = money
    stock_n = 0
    for stock in stocks:
        stock_n += left_money // stock
        left_money %= stock
        if left_money == 0:
            break
    return left_money, stock_n

def sungmin():
    left_money = money
    stock_n = 0
    for i in range(len(stocks) - 4):
        if stocks[i] < stocks[i + 1] < stocks[i + 2] < stocks[i + 3]:
            left_money += stock_n * stocks[i + 3]
            stock_n = 0
        if stocks[i] > stocks[i + 1] > stocks[i + 2] > stocks[i + 3]:
            stock_n += left_money // stocks[i + 3]
            left_money %= stocks[i + 3]
    return left_money, stock_n

jun_money, jun_n = junhyun()
sun_money, sun_n = sungmin()

total_jun = jun_money + stocks[-1] * jun_n
total_sung = sun_money + stocks[-1] * sun_n

if total_jun > total_sung:
    print('BNP')
elif total_jun < total_sung:
    print('TIMING')
else:
    print("SAMESAME")
