# 백준 1966. 프린터 큐
# https://www.acmicpc.net/problem/1966

############################## 문제 이해 ##############################
# 프린터 기기는 명령을 받은 '순서대로' 인쇄한다. -> queue
# 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.
# 1. 현재 Queue의 가장 앞에 있눈 문서의 '중요도'를 확인
# 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄
# 하지 않고 Queue의 가장 뒤에 배치, 그렇지 않다면 바로 인쇄
############################## 문제 이해 ##############################
############################## 알고리즘 ##############################
# 입력:
# 문서의 개수 N 과 M
# M: 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여있는지를 나타내는 정수
# 맨 왼쪽은 0번째임
# N개의 문서도의 중요도가 차례대로 주어짐, 중요도는 1이상 9이하의 정수

# 출력
# 각 테스트 케이스에 대해 문서가 몇번째로 인쇄되는지 출력



############################## 알고리즘 ##############################
from collections import deque
def print_order(N, M, priorities):
    order = 1

    while True:
        current = priorities.popleft()

        if any(current[1] < p[1] for p in priorities):
            priorities.append(current)
        else:
            if current[0] == M:
                print(order)
                return
            order += 1

def main():
    T = int(input().strip())

    for _ in range(T):
        N, M = map(int, input().split())
        priorities = deque(enumerate(map(int, input().split())))
        print_order(N, M, priorities)

if __name__ == '__main__':
    main()