# 백준 1759. 암호 만들기
# https://www.acmicpc.net/problem/1759
########################### 완전 탐색 (조합) ############################
import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
chars = sorted(sys.stdin.readline().strip().split())
def sol(L, chars):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    for comb in combinations(chars, L):
        num_vowels = sum(1 for c in comb if c in vowels)
        num_consonants = L - num_vowels
        
        if num_vowels >= 1 and num_consonants >=2:
            print(''.join(comb))
sol(L=L, chars=chars)
########################### 완전 탐색 (조합) ############################

########################### 백트래킹 ############################
import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
chars = sorted(sys.stdin.readline().strip().split())
vowels = {'a', 'e', 'i', 'o', 'u'}
def backtrack(idx, password, num_vowels, num_consonants):
    
    if len(password) == L:
        if num_vowels >= 1 and num_consonants >= 2:
            print(''.join(password))
        return
    
    for i in range(idx, C):
        char = chars[i]
        if char in vowels:
            backtrack(i + 1, password + [char], num_vowels + 1, num_consonants)
        else:
            backtrack(i + 1, password + [char], num_vowels, num_consonants + 1)

backtrack(0, [], 0, 0)            
########################### 백트래킹 ############################