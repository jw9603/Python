# 백준 2775. 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775
############################## 문제 이해 ##############################
# 반상회를 주최하려고 한다.
# 아파트 거주조건: a층의 b호에 살려면 자신의 아래층의 1호부터 b호까지 사람들의 수의 합만큼
# 데려와 살아야 한다.
# 아파트에 비어있는 집은 없다. 모든 거주민들이 계약 조건을 지키고 왔다고 가정했을 때,
# 주어지는 양의 정수 k와 n에 대해 k층 n호에는 몇 명이 살고 있는지 출력하라.
# 아파트에는 0층부터 있고 각 층에는 1호부터 있다. 0층의 i호에는 i명이 산다.
############################## 문제 이해 ##############################
# 1. 완전탐색: 재귀
# def cnt_people(k, n):
#     if k == 0:
#         return n
    
#     cnt = 0

#     for i in range(1, n + 1):
#         cnt += cnt_people(k - 1, i)
    
#     return cnt

# def main():
#     T = int(input().strip())
#     for _ in range(T):
#         k = int(input().strip())
#         n = int(input().strip())
#         print(cnt_people(k, n))

# if __name__ == '__main__':
#     main()

def cnt_people(k, n): # k층 n호에 거주하는 사람 수
    people = [i for i in range(1, n + 1)]
    
    for _ in range(k):
        for j in range(1, n): 
            people[j] += people[j - 1]
    return people[-1]


def main():
    T = int(input().strip())
    for _ in range(T):
        k = int(input().strip())
        n = int(input().strip())
        print(cnt_people(k, n))

if __name__ == '__main__':
    main()