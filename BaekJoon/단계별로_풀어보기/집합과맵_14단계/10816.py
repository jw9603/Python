# 10816. 숫자 카드 2
# https://www.acmicpc.net/problem/10816

import sys

N = int(sys.stdin.readline().strip())
card = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
num = list(map(int,sys.stdin.readline().split()))

def sol(card, num):
    
    dict_card = {}
    result = []
    for i in card:
        if i in dict_card:
            dict_card[i] += 1
        else:
            dict_card[i] = 1
    
    for i in num:
        if i in dict_card:
            result.append(dict_card[i])
        else:
            result.append(0)
    return ' '.join([str(i) for i in result])

print(sol(card=card, num=num))
    