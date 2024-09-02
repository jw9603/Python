import sys

A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())

print(A+B-C,int(str(A)+str(B))-C,sep='\n')