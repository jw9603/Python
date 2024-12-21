# 백준 1541. 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
import sys
equation = sys.stdin.readline().strip().split('-')
def sol(eq):
    num = []
    for i in eq:
        tmp = i.split('+')
        total = 0
        for j in tmp:
            total += int(j)
        num.append(total)
    print(num[0] + sum(-i for i in num[1:]))
sol(eq=equation)