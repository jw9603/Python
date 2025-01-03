# 백준 9046. 복호화
# https://www.acmicpc.net/problem/9046
import sys
from collections import Counter
T = int(sys.stdin.readline().strip())
for _ in range(T):
    s = sys.stdin.readline().strip()
    s = s.replace(' ','')
    cnt = sorted(Counter(s).items(), key=lambda x:x[1], reverse=True) # Counter(s).most_common()이란 함수를 기억하자.
    if len(cnt) == 1:
        print(cnt[0][0])
        continue
    if cnt[0][1] == cnt[1][1]:
        print('?')
    else:
        print(cnt[0][0])