import sys

num = list(map(int,sys.stdin.readline().split()))
print(sum(i ** 2 for i in num) % 10)