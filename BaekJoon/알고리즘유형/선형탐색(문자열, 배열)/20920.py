# 백준 20920. 영단어 암기는 괴로워
# https://www.acmicpc.net/problem/20920
import sys
from collections import Counter
N, M = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().strip() for _ in range(N)]
def sol(N, M, words):
    words = [word for word in words if len(word) >= M]
    word_cnt = Counter(words)
    sorted_words = sorted(word_cnt.keys(), key=lambda x:(-word_cnt[x], -len(x), x))
    return '\n'.join(sorted_words)
print(sol(N=N, M=M, words=words))
    