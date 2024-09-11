# 1541 - 잃어버린 괄호
# https://www.acmicpc.net/problem/1541

# 사칙연산 중 주어지는 것은 "+"와 "-" 뿐.. 
# 우리가 해야할 것은 괄호를 어디다 해서 값이 최소가 되도록 만드는 것

import sys

def sol(expression):
    num = []
    for i in expression:
        tot = 0
        tmp = i.split('+')
        for j in tmp:
            tot += int(j)
        num.append(tot)
    return num[0] + sum([-i for i in num[1:]])

expression = sys.stdin.readline().strip().split('-')

print(sol(expression))


