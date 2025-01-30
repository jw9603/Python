# 백준 1620. 나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620
import sys
N, M = map(int, sys.stdin.readline().split())
names = [sys.stdin.readline().strip() for _ in range(N)]
name_dict = {}   # 포켓몬 이름이 key
number_dict = {} # 포켓몬 이름의 번호가 key
for i, name in enumerate(names):
    name_dict[name] = i + 1
    number_dict[i + 1] = name
def sol(name_dict, number_dict, x):
    if x.isdigit():
        print(number_dict[int(x)])
    else:
        print(name_dict[x])
            
for _ in range(M):
    x = sys.stdin.readline().strip()
    sol(name_dict=name_dict, number_dict=number_dict, x=x)
        
    