# 백준 1213. 팰린드롬 만들기
# https://www.acmicpc.net/problem/1213
import sys
from collections import Counter
name = sys.stdin.readline().strip()
def sol(name):
    odd_cnt = 0
    odd_char = None
    left = []
    counter = Counter(name)
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
print(sol(name=name))
            