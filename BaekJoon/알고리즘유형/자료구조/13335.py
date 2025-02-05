# 백준 13335. 트럭
# https://www.acmicpc.net/problem/13335
import sys
from collections import deque
n, w, L = map(int, sys.stdin.readline().split())
trucks = list(map(int, sys.stdin.readline().split()))

def sol(w, L, trucks):
    bridge = deque([0] * w)
    bridge_weight = 0
    time = 0
    
    for truck in trucks:
        
        while True:
            time += 1
            bridge_weight -= bridge.popleft()
            
            if truck + bridge_weight <= L:
                bridge.append(truck)
                bridge_weight += truck
                break
            else:
                bridge.append(0)
    time += w
    return time
print(sol(w=w, L=L, trucks=trucks))