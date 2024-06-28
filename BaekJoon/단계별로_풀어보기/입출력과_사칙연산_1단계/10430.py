import sys

A,B,C = map(int,sys.stdin.readline().split())
print('\n'.join(map(str,[(A+B)%C,((A%C) + (B%C))%C,(A*B)%C,((A%C) * (B%C))%C])))