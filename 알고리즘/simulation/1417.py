# 백준 1417. 국회의원 선거
# https://www.acmicpc.net/problem/1417
################################# 문제 이해 #################################
# 다솜이의 기계는 각 사람들이 누구를 찍을 지 미리 읽을 수 있다.
# 어떤 사람이 누구를 찍을 지 정했으면, 반드시 선거때 그 사람을 찍는다.
# 현재 국회의원 후보는 N명, 다솜이는 이 기계를 이용해서 그 마을의 주민 M명의 마음을 모두 읽었다.
# 다솜이는 기호 1번이다.

# 다솜이는 사람들의 마음을 읽어서 자신을 찍지 않으려는 사람을 돈으로 매수해서 국회의원에 당선
# 이 되게 하려고 한다. 다른 모든 사람의 득표수보다 많은 득표수를 가질 때, 그 사람이 국회의원에 당선

# 다솜이가 매수해야하는 사람의 최솟값을 출력하는 프로그램을 작성해라.

# 입력
# 첫째 줄에 후보의 수 N명, 둘째 줄부터 차례대로 기호 1 ~ 기호 N번을 찍으려고 하는 수

# 출력
# 첫째 줄에 다솜이가 매수해야 하는 사람의 최솟값

# 알고리즘
# 1 <= N <= 50, 1 <= 득표수 <= 100
# 매수해야하는 사람의 최솟값을 구해야 한다. 최솟값이기 때문에,, 다솜이보다 득표수가 높은 사람의 표를
# 가장 먼저 매수해야한다.
# 가장 득표수가 많은 사람을 1명씩 매수할때마다, 다시 정렬을 해서 가장 높은 사람의 수를 파악해야 한다.
# 이뜻은 매번 정렬을 진행하기 때문에 max_heap을 사용해야 한다.

################################# 문제 이해 #################################
# 1. 매번 정렬
def sol(n, votes, dasom):
    cnt = 0
    votes.sort(reverse=True)

    if n == 1:
        return 0
    else:
        while votes[0] >= dasom:
            dasom += 1
            votes[0] -= 1
            cnt += 1
            votes.sort(reverse=True)
    return cnt

def main():
    N = int(input().strip())
    dasom = int(input().strip())
    votes = [int(input().strip()) for _ in range(N - 1)]

    print(sol(N, votes, dasom))

if __name__ == '__main__':
    main()

# 2. Heap
from heapq import heappush, heappop, heapify
def sol(n, votes, dasom):
    votes = [-v for v in votes]
    heapify(votes)
    cnt = 0

    if n == 1:
        return 0
    
    while votes and -votes[0] >= dasom:
        max_votes = -heappop(votes)
        max_votes -= 1
        dasom += 1
        cnt += 1
        heappush(votes, -max_votes)

    return cnt

def main():
    N = int(input().strip())
    dasom = int(input().strip())
    votes = [int(input().strip()) for _ in range(N - 1)]

    print(sol(N, votes, dasom))

if __name__ == '__main__':
    main()