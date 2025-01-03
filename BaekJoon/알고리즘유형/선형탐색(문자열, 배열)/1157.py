# 백준 1157. 단어 공부
# https://www.acmicpc.net/problem/1157


################# 내 풀이 #################
import sys
from collections import Counter
s = sys.stdin.readline().strip().lower()
cnt = Counter(s).most_common()
if len(cnt) <= 1:
    print(cnt[0][0].upper())
elif cnt[0][1] == cnt[1][1]:
    print('?')
else:
    print(cnt[0][0].upper())
################# 내 풀이 #################


################# 다른 풀이 #################
import sys
s = sys.stdin.readline().strip()
def sol(s):
    s = s.upper()
    alphabet_cnt = [0] * 26
    for char in s:
        index = ord(char) - ord('A')
        alphabet_cnt[index] += 1
    
    max_cnt = max(alphabet_cnt)
    max_index = [i for i, cnt in enumerate(alphabet_cnt) if cnt == max_cnt]
    
    if len(max_index) > 1:
        return '?'
    else:
        return chr(max_index[0] + ord('A'))
print(sol(s=s))
################# 다른 풀이 #################