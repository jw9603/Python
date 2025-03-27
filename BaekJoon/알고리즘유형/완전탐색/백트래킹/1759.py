# 백준 1759. 암호 만들기
# https://www.acmicpc.net/problem/1759
################################## 백트래킹 ##################################
import sys
def dfs(idx, password, num_vowels, num_consonant):
    global L, C, chars, vowels

    # 1. base case
    if len(password) == L:
        if num_vowels >= 1 and num_consonant >= 2:
            print(''.join(password))
        return
    
    for i in range(idx, C):
        c = chars[i]

        if c in vowels:
            dfs(i + 1, password + [c], num_vowels + 1, num_consonant)
        else:
            dfs(i + 1, password + [c], num_vowels, num_consonant + 1)


def main():
    global L, C, chars, vowels
    L, C = map(int, sys.stdin.readline().split())
    chars = sorted(sys.stdin.readline().strip().split())
    vowels = {'a', 'e', 'i', 'o', 'u'}

    dfs(0, [], 0, 0)

if __name__ == '__main__':
    main()
################################## 백트래킹 ##################################

################################## itertools ##################################
import sys
from itertools import combinations
def print_password(L, chars):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for comb in combinations(chars, L):
        num_vowels = sum(1 for c in comb if c in vowels)
        num_consonant = L - num_vowels

        if num_vowels >= 1 and num_consonant >= 2:
            print(''.join(comb))

def main():

    L, C = map(int, sys.stdin.readline().split())
    chars = sorted(sys.stdin.readline().strip().split())
    
    print_password(L, chars)

if __name__ == '__main__':
    main()
################################## itertools ##################################