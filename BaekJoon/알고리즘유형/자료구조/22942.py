# 백준 22942, 데이터 체커
# https://www.acmicpc.net/problem/22942
import sys
N = int(sys.stdin.readline().strip())
circles = []
for i in range(N):
    x, r = map(int, sys.stdin.readline().split())
    circles.append((x - r, i, 0))
    circles.append((x + r, i, 1))
    
def sol(circles):
    circles.sort()
    stack = []
    
    for i in range(len(circles)):
        if circles[i][2] == 0:
            stack.append(circles[i][1])
        else:
            if circles[i][1] == stack[-1]:
                stack.pop()
            else:
                return 'NO'
    return 'YES' if not stack else 'NO'
print(sol(circles=circles))