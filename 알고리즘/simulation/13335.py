# 백준 13335. 트럭
# https://www.acmicpc.net/problem/13335
############################## 문제 이해 ##############################
# 다리 하나가 있다. 이 다리를 n 개의 트럭이 건너가려고 한다.
# 트럭의 순서는 바꿀 수 없으며, 트럭의 무게는 서로 같지 않을 수 있다.
# 다리 위에는 단지 w대의 트럭만 동시에 올라갈 수 있다.
# 다리의 길이는 w 길이이며, 각 트럭들은 하나의 시간에 하나의 길이만큼 이동할 수 있다고 가정
# 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다.

# 입력
# 첫 번째 줄에는 세 개의 정수 n, w, L이 주어진다.
# n: 다리를 건너는 트럭의 수, w: 다리의 길이, L: 다리의 최대하중
# 두 번째 줄에는 n개의 정수 a1, ..., an이 주어지고, ai는 i번째 트럭의 무게

# 알고리즘
# 다리는 deque = deque([0] * w) # w길이
# time = 0
# for truck in trucks:
#    while True
#     time += 1
#     bridget_weight -= deque.popleft()
#     if truck + bridge_weight <= L:
#         # bridges.append(truck)
#           bridge_weight += truck
            # break
#      else:
#          bridge.append(0)

# time += w
# return time
############################## 문제 이해 ##############################
from collections import deque
def min_time(n, w, L, trucks):
    bridge = deque([0] * w)
    bridge_weight = 0
    time = 0

    for truck in trucks:
        while True:
            time += 1
            bridge_weight -= bridge.popleft()
            if bridge_weight + truck <= L:
                bridge.append(truck)
                bridge_weight += truck
                break
            else:
                bridge.append(0)
    
    time += w
    
    return time

def main():
    n, w, L = map(int, input().split())
    trucks = list(map(int, input().split()))

    print(min_time(n, w, L, trucks))

if __name__ == '__main__':
    main()