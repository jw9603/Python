# 백준 10799. 쇠막대기
# https://www.acmicpc.net/problem/10799
import sys
ps = sys.stdin.readline().strip()
def sol(ps):
    stack = []
    cnt = 0
    
    for i in range(len(ps)):
        if ps[i] == '(':
            stack.append(ps[i])
        else:
            if ps[i - 1] == '(':
                stack.pop()
                cnt += len(stack)
            else:
                stack.pop()
                cnt += 1
    return cnt
print(sol(ps=ps))
