import sys

print(''.join([i.upper() if i.islower() else i.lower() for i in sys.stdin.readline().strip()]))