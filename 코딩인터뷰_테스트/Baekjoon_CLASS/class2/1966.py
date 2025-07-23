# 백준 1966. 프린터 큐
# https://www.acmicpc.net/problem/1966
####################################### 문제 이해 #######################################
# 상근이는 새로운 프린터기 내부 소프트웨어를 개발, 이 프린터기는 다음과 같은 조건에 따라 인쇄
# 1. 현재 Queue의 가장 앞에 있는 문서의 중요도를 확인
# 2. 현재 Queue에서 가장 앞에 있는 문서보다 중요도가 높은 문서가 하나라도 있다면,
#    현재 Queue의 가장 앞에 있는 문서를 Queue의 가장 뒤로 보냄, 그렇지 않다면 바로 인쇄
# 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는 지 알아내는 것.

# 입력:
# 첫째 줄에 테스트 케이스의 개수 T가 주어짐
# 각 테스트 케이스의 첫째 줄에는 문서의 개수 N과 몇 번째로 인쇄되었는 지 궁금한 문서가 현재 큐에 몇 번째에 놓여있는지를
# 나타내는 정수 M이 주어짐(맨 왼쪽은 0번쨰)
# 둘째 줄에는 N개의 문서의 중요도가 주어짐, 중요도는 1이상 9이하의 정수

# 출력: 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되었는지 출력

# 알고리즘
# 1. 각 테스트 케이스에 대해 큐를 생성
# 2. 큐에 문서의 중요도와 인덱스를 함께 저장
# 3. 큐의 가장 앞에 있는 문서의 중요도를 확인
# 4. 현재 큐에서 가장 앞에 있는 문서보다 중요노가 높은 문서가 있는지 확인
# 5. 만약 있다면, 현재 문서를 큐의 뒤로 보내고
# 6. 만약 없다면, 현재 문서를 인쇄하고 인쇄 순서를 증가시킴
# 7. 만약 인쇄한 문서가 M번째 문서라면, 인쇄 순서를 출력하고 종료
####################################### 문제 이해 #######################################
from collections import deque
def sol(queue, M):
    print_order = 0

    while queue:
        current = queue.popleft()
        if any(current[0] < doc[0] for doc in queue):
            queue.append(current)
        else:
            print_order += 1
            if current[1] == M:
                return print_order

def main():
    T = int(input().strip())
    for _ in range(T):
        N, M = map(int, input().strip().split())
        queue = deque([(x, i) for i, x in enumerate(map(int, input().strip().split()))])
        print(sol(queue, M))

if __name__ == "__main__":
    main()