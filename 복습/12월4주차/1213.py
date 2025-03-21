# 백준 1213. 팰린드롬 만들기
# https://www.acmicpc.net/problem/1213
import sys
from collections import Counter
def sol(name):
    odd_char = 'None'
    odd_cnt = 0
    counter = Counter(name)
    left = []
    for char in sorted(counter.keys()):
        count = counter[char]
        if count % 2 == 1:
            odd_cnt += 1
            odd_char = char
            if odd_cnt > 1:
                return "I'm Sorry Hansoo"
        left.append(char * (count // 2))
    left = ''.join(left)
    center = odd_char if odd_cnt == 1 else ''
    right = left[::-1]
    return ''.join([left, center, right])
name = sys.stdin.readline().strip()
print(sol(name=name))
            