# 위에서 아래로
import sys
N = int(sys.stdin.readline().strip())
print(*sorted([int(sys.stdin.readline().strip()) for _ in range(N)], reverse=True))