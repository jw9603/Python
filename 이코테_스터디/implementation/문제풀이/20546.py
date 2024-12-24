# 백준 20546. 기적의 매매법
# https://www.acmicpc.net/problem/20546
import sys
money = int(sys.stdin.readline().strip())
stock_price = list(map(int, sys.stdin.readline().split()))

def junhyun():
    left_money = money
    stock_n = 0
    for stock in stock_price:
        stock_n += left_money // stock
        left_money %= stock
        if left_money == 0:
            break
    return left_money, stock_n
        
def sungmin():
    left_money = money
    stock_n = 0
    # 도든 거래는 전량 매수와 전량 매도
    # 3일 연속 가격이 전일 대비 상승하는 주식은 다음날 무조건 가격이 하락한다고 가정한다.
    # 따라서 현재 소유한 주식의 가격이 3일째 상승한다면, 전량 매도
    # 3일 연속 가격이 전일 대비 하락하는 주식은 다음날 무조건 가격이 상승한다고 가정한다.
    # 따라서 이러한 경향이 나타나면 즉시 주식을 전량 매수
    for i in range(len(stock_price) - 4):
        if stock_price[i] < stock_price[i + 1] < stock_price[i + 2] < stock_price[i + 3]:
            left_money += stock_n * stock_price[i + 3]
            stock_n = 0
        
        if stock_price[i] > stock_price[i + 1] > stock_price[i + 2] > stock_price[i + 3]:
            stock_n += left_money // stock_price[i + 3]
            left_money %= stock_price[i + 3]
    return left_money, stock_n

jun_money, jun_n = junhyun()
sung_money, sung_n = sungmin()


# 자산 계산 = (left_money + stock_price[-1] * stock_n)
total_jun = jun_money + stock_price[-1] * jun_n
total_sung = sung_money + stock_price[-1] * sung_n

if total_jun > total_sung:
    print('BNP')
elif total_jun < total_sung:
    print('TIMING')
else:
    print('SAMESAME')

               
