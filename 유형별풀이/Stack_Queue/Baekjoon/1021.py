# 1021번 - 회전하는 큐
# https://www.acmicpc.net/problem/1021

                
import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())

queue = deque([i+1 for i in range(N)])

position = list(map(int,sys.stdin.readline().split()))

cnt = 0

for i in position:
    
    while True:
        
        if queue[0] == i:
            queue.popleft()
            break
        
        else:
            if queue.index(i) <= len(queue) // 2:
                while queue[0] != i:
                    queue.rotate(-1)
                    cnt += 1
            else:
                while queue[0] != i:
                    queue.rotate(1)
                    cnt += 1
print(cnt)
            
