# 백준 1092. 배
# https://www.acmicpc.net/problem/1092

############################ 시간초과 ###########################
# import sys
# N = int(sys.stdin.readline().strip())
# cranes = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline().strip())
# boxes = list(map(int, sys.stdin.readline().split()))
# def sol(cranes, boxes):
#     cranes.sort(reverse=True)
#     boxes.sort(reverse=True)
    
#     if cranes[0] < boxes[0]:
#         return -1
    
#     time = 0
#     while boxes:
#         time += 1
#         for crane in cranes:
#             for i in range(len(boxes)):
#                 if boxes[i] <= crane:
#                     boxes.pop(i)
#                     break
#     return time
# print(sol(cranes=cranes, boxes=boxes))
############################ 시간초과 ###########################
def sol(N, cranes, boxes):
    cranes.sort(reverse=True)  # 크레인을 무거운 순으로 정렬
    boxes.sort(reverse=True)   # 박스를 무거운 순으로 정렬
    
    if cranes[0] < boxes[0]:  # 가장 무거운 박스를 옮길 수 없으면 -1 반환
        return -1
    time = 0

    while boxes: # 7, 5, 4, 2, 2
        time += 1
        idx = 0 # 크레인 인덱스
        i = 0   # 박스 인덱스
        
        while idx < N and i < len(boxes):
            if cranes[idx] >= boxes[i]:
                boxes.pop(i)
                idx += 1
            else:
                i += 1
    return time
# 입력 처리
import sys
N = int(sys.stdin.readline().strip())
cranes = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
boxes = list(map(int, sys.stdin.readline().split()))

# 결과 출력
print(sol(N=N, cranes=cranes, boxes=boxes))
