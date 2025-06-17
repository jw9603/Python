# 백준 20546. 기적의 매매법
# https://www.acmicpc.net/problem/20546
##################################### 문제 이해 #####################################
# 준현, 성민 
# 준현: BNP전략, 주식을 살 수 있다면 무조건 최대한 많이 산다. 즉, 가능한 만큼 즉시 매수
# 성민: 33매매법, 
# 모든 거래는 전량 매수와 전량 매도, 3일 연속 가격이 전일 대비 상승하는 주식은 다음날 무조건
# 가격이 하락한다고 가정, 따라서 현재 소유한 주식의 가격이 3일째 상승한다면, 전량 매도
# 반대로 3일 연속 가격이 전일 대비 하락하는 주식은 다음날 무조건 가격이 상승한다고 가정,
# 이러한 경향이 나타나면 즉시 주식을 매수한다.

# 기간은 2021년 1월 1일부터 1월 14일까지 누가 더 높은 수익률?

# 입력
# 첫 번째 줄에 준현이와 성민이에게 주어진 현금이 주어진다.
# 두 번째 줄에 1월 1일부터 1월 14일까지의 주가가 공백을 두고 차례대로 주어진다.

# 출력
# 준현이의 자산이 더 크다면 BNP, 성민이의 자산이 더 크다면 TIMING을 출력
# 같다면 SAMESAME 출력

# 알고리즘
# 함수 2개를 만든다. 각 함수는 준현, 성민의 전략을 나타내는 함수들

##################################### 문제 이해 #####################################
def junhyun(stocks, money):
    stock_n = 0
    left_money = money

    for stock in stocks:
        stock_n += left_money // stock
        left_money %= stock
        if left_money == 0:
            break
    
    return left_money, stock_n

def sungmin(stocks, money):
    stock_n = 0
    left_money = money

    for i in range(len(stocks) - 4):
        if stocks[i] < stocks[i + 1] < stocks[i + 2] < stocks[i + 3]:
            left_money += stock_n * stocks[i + 3]
            stock_n = 0
        if stocks[i] > stocks[i + 1] > stocks[i + 2] > stocks[i + 3]:
            stock_n += left_money // stocks[i + 3]
            left_money %= stocks[i + 3]
    
    return left_money, stock_n

def sol(money, stocks):
    jun_money, jun_n = junhyun(stocks, money)
    sung_money, sung_n = sungmin(stocks, money)

    total_jun = jun_money + stocks[-1] * jun_n
    total_sung = sung_money + stocks[-1] * sung_n

    if total_jun > total_sung:
        return 'BNP'
    elif total_jun < total_sung:
        return 'TIMING'
    else:
        return 'SAMESAME'

def main():
    money = int(input().strip())
    stocks = list(map(int, input().split()))

    print(sol(money, stocks))

if __name__ == '__main__':
    main()