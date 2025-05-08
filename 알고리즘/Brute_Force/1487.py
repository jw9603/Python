# 백준 1487. 물건 팔기
# https://www.acmicpc.net/problem/1487
################################ 문제 이해 ################################
# 신상품을 최대 이익에 팔려고 한다.
# N명이나 살 의향을 보였다.
# 각각의 사람은 자기가 지불할 생각이 있는 최대 한도가 있다.
# N명의 사람과, 각각의 사람이 지불할 용의가 있는 최대 금액과 배송비가 주어졌을 때,
# 세준이의 이익을 최대로 하는 가격
################################ 문제 이해 ################################
def sol(N, costs):
    costs.sort()

    max_price = 0  # 세준이의 이익을 최대로 하는 가격
    max_profit = 0 # 최대 이익값 합

    for i in range(N):
        price = costs[i][0] # 현재 가격
        profit = 0          # 이 때의 이익의 합 변수

        for j in range(i, N): 
            if price > costs[j][1]:
                profit += (price - costs[j][1])
        
        if profit > max_profit:
            max_profit = profit
            max_price = price
    
    return max_price

def main():
    N = int(input().strip())
    costs = [list(map(int, input().split())) for _ in range(N)]

    print(sol(N, costs))

if __name__ == '__main__':
    main()