# 백준 9375. 패션왕 신해빈
# https://www.acmicpc.net/problem/9375
#################################### 문제 이해 ####################################
# 해빈이는 패션에 매우 민감해서 한 번 입었던 옷들의 조합을 절대 다시 입지 않는다.
# 해빈이가 가진 의상들이 주어졌을 때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?

# 입력:
# 첫째 줄에 테스트 케이스가 주어짐.
# 각 테스트 케이스의 첫째 줄에는 해빈이가 가진 의상의 수 n이 주어진다.
# 다음 n개에는 해빈이가 가진 의상의 이름과 의상의 종류가 공백으로 구분되어 주어진다.

# 출력: 각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로 의상을 입을 수 있는 경우를 출력하시오.

# 알고리즘
# 딕셔너리를 생성한다.
# 딕셔너리의 키는 의상의 종류, 값은 의상의 이름이 주어진다.
# value 개수 총합 + 각 value 개수 곱하기 == (value 개수 + 1) 곱한다음 - 1
#################################### 문제 이해 ####################################
from collections import defaultdict
def sol(wears):
    cnt = 1

    for type in wears:
        cnt *= (len(wears[type]) + 1)
    
    return cnt - 1

def main():
    T = int(input().strip())
    
    for _ in range(T):
        n = int(input().strip())
        wears = defaultdict(list)
        for _ in range(n):
            name, type = input().split()

            if type in wears:
                wears[type].append(name)
            else:
                wears[type] = [name]

        print(sol(wears))

if __name__ == '__main__':
    main()