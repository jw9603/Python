# 백준 1181. 단어 정렬
# https://www.acmicpc.net/problem/1181
import sys
N = int(sys.stdin.readline().strip())
words = set([sys.stdin.readline().strip() for _ in range(N)])
print('\n'.join(sorted(words, key=lambda x:(len(x), x))))