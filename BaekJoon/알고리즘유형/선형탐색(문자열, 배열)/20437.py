# 백준 20437. 문자열 게임 2
# https://www.acmicpc.net/problem/20437
import sys
from collections import defaultdict
T = int(sys.stdin.readline().strip())
def sol(T):
    for _ in range(T):
        W = sys.stdin.readline().strip()
        K = int(sys.stdin.readline().strip())
        word_dict = defaultdict(list)
        for i in range(len(W)):
            if W.count(W[i]) >= K:
                word_dict[W[i]].append(i)
        
        min_val = 10 ** 5
        max_val = -1
        if word_dict:
            for word_idx in word_dict.values():
                for i in range(len(word_idx)- K + 1):
                    check_len = word_idx[i + K - 1] - word_idx[i] + 1
                    min_val = min(min_val, check_len)
                    max_val = max(max_val, check_len)
            print(min_val, max_val)
        else:
            print(-1)
sol(T=T)
        
            