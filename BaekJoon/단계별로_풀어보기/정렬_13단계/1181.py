# 1181 - 단어 정렬
# https://www.acmicpc.net/problem/1181

import sys

N = int(sys.stdin.readline().strip())
word_list = []

for _ in range(N):
    word_list.append(sys.stdin.readline().strip())
    
word_list = list(set(word_list))   
def sol(word_list):
    word_list.sort(key=lambda x: (len(x),x))
    
    print('\n'.join(i for i in word_list))
    
sol(word_list=word_list)