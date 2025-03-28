# 백준 6603. 로또
# https://www.acmicpc.net/problem/6603

############################ 백트래킹 ############################
import sys
def dfs(start, curr, S):
    if len(curr) == 6:
        print(' '.join(map(str, curr)))
        return
    
    for i in range(start, len(S)):
        curr.append(S[i])
        dfs(i + 1, curr, S)
        curr.pop()

def main():
    while True:
        data = list(map(int, sys.stdin.readline().split()))
        
        if data[0] == 0:
            break

        S = data[1:]

        dfs(0, [], S)
        print()

if __name__ == '__main__':
    main()
############################ 백트래킹 ############################

############################ itertools ############################
import sys
from itertools import combinations
def sol(S):
    for comb in combinations(S, 6):
        print(' '.join(map(str, comb)))

def main():
    while True:
        data = list(map(int, sys.stdin.readline().split()))
        
        if data[0] == 0:
            break

        S = data[1:]

        sol(S)
        print()

if __name__ == '__main__':
    main()
############################ itertools ############################