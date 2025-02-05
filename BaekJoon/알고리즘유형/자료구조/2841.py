# 백준 2841. 외계인의 기타 연주
# https://www.acmicpc.net/problem/2841
import sys
N, P = map(int, sys.stdin.readline().split())
melodies = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def sol(melodies):
    cnt = 0
    stack = {i:[] for i in range(1, 7)}
    for line, pret in melodies:
        
        while stack[line] and stack[line][-1] > pret:
            stack[line].pop()
            cnt += 1
        
        if not stack[line] or stack[line][-1] < pret:
            stack[line].append(pret)
            cnt += 1
    return cnt
print(sol(melodies=melodies))