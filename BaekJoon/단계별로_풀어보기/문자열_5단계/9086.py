import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    munja = sys.stdin.readline().strip()
    if len(munja) != 1:
        print(munja[0],munja[-1],sep='')
    else:
        print(munja[0]*2)