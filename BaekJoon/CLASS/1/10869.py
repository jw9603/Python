import sys
a,b = map(int,sys.stdin.readline().split())

print('\n'.join(map(str,[a+b,a-b,a*b,int(a/b),int(a%b)])))