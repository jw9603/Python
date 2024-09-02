import sys

N = int(sys.stdin.readline().strip())
num = sys.stdin.readline().strip()
tot = 0
for i in num:
    tot += int(i)
print(tot)