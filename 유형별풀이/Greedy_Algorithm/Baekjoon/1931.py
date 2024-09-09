# 1931 - 회의실 배정
# https://www.acmicpc.net/problem/1931

# 회의가 빨리 끝나야 많이 때려 넣을 수 있음
import sys

def meeting_room(tt):
    tt.sort(key=lambda x: (x[1],x[0]))
    
    new_end = 0
    ans = 0
    
    for i,j in tt:
        if new_end <= i:
            ans += 1
            new_end = j
            
    return ans

N = int(sys.stdin.readline().strip()) # 회의의 수
tt = []

for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    tt.append((x,y))
    
print(meeting_room(tt))

