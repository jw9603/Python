# 백준 5032. 탄산 음료
# https://www.acmicpc.net/problem/5032


################# 재귀를 사용한 풀이 ##################
import sys
e, f, c = map(int, sys.stdin.readline().split())
def sol(bottles, c, total_drinks=0):
    if bottles < c:
        return total_drinks
    
    drinks = bottles // c
    return sol(bottles % c + drinks, c, total_drinks + drinks)

print(sol(bottles= e + f, c=c))
################# 재귀를 사용한 풀이 ##################

################# 반복문을 사용한 풀이 ##################
import sys
e, f, c = map(int, sys.stdin.readline().split())

def sol(e, f, c):
    total_drinks = 0
    bottles = e + f
    while bottles >= c:
        drinks = bottles // c
        total_drinks += drinks
        bottles = bottles % c + drinks
    return total_drinks
print(sol(e=e, f=f, c=c))
################# 반복문을 사용한 풀이 ##################