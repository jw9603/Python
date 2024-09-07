# 2720 - 세탁소 사장 동혁
# https://www.acmicpc.net/problem/2720

import sys

# 테스트 케이스의 수 입력
T = int(sys.stdin.readline().strip())

# 각 테스트 케이스에 대해 처리
for _ in range(T):
    # 거스름돈 입력 (센트 단위)
    charge = int(sys.stdin.readline().strip())
    
    # 동전의 단위에 맞춰 개수 계산
    for i in [25, 10, 5, 1]:
        print(charge // i, end=' ')  # 동전의 개수를 출력
        charge %= i  # 나머지 금액 갱신
    print()  # 다음 테스트 케이스 출력을 위해 줄바꿈