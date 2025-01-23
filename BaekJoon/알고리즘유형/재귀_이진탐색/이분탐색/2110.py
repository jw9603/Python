# 백준 2110. 공유기 설치
# https://www.acmicpc.net/problem/2110
import sys
N, C = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline().strip()) for _ in range(N)]

def can_install_routers(houses, C, distance):
    cnt = 1
    tmp = houses[0]
    for house in houses[1:]:
        if house - tmp >= distance:
            cnt += 1
            tmp = house
        if cnt >= C:
            return True
    return False

def sol(N, C, houses):
    houses.sort()
    left, right = 1, houses[-1] - houses[0]
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if can_install_routers(houses, C, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

print(sol(N=N, C=C, houses=houses))
            