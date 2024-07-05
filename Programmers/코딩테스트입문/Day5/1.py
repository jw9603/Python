def solution(price):
    if price >= 500000:
        return int(price * 0.80)
    elif price >= 300000 and price < 500000:
        return int(price * 0.90)
    elif price >= 100000 and price < 300000:
        return int(price * 0.95)
    else:
        return int(price) # 10만원 이하인 경우는 할인을 안받는다. 이 경우를 생각해야 한다.
    
if __name__ =='__main__':
    print(solution(150000))
    print(solution(580000))
    print(solution(90000))