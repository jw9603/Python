# 백준 2941. 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941
import sys
word = sys.stdin.readline().strip()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for char in croatia:
    word = word.replace(char,'!')
print(len(word))