import sys

S = sys.stdin.readline().strip()

for i in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(i),end=' ')