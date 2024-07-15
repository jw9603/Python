import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    A, B = map(int,sys.stdin.readline().split())
    print(f'Case #{i+1}: {A} + {B} = {A+B}')