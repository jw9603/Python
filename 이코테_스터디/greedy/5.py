# 이코테 그리디 - 모험가 길드
import sys

N = int(sys.stdin.readline().strip())

card = list(map(int, sys.stdin.readline().split()))

card.sort()

cnt = 0
result = 0

for i in card:
    cnt += 1  # 현재 그룹에 포함된 모험가 수 증가
    
    # 현재 그룹에 포함된 모험가 수가 현재 모험가의 공포도 이상이면 그룹 결성
    if cnt >= i:
        result += 1  # 그룹 수 증가
        cnt = 0  # 현재 그룹 모험가 수 초기화
print(result)

    