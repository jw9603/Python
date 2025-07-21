# 백준 2775. 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775
################################ 문제 이해 ################################
# 반상회를 주최하려고 한다.
# a층의 b호에 살려면 자신의 아래(a - 1)층의 1호부터 b호까지 사람들의 수의 합만큼 
# 사람들을 데려와 살아야 한다.

# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때,
# 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력
# 아파트에는 0층부터 있고 각 층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

# 알고리즘

# 0층의 1호부터 i호에는 각 호수명만큼산다.
################################ 문제 이해 ################################
def sol(k, n):
    people = [x for x in range(1, n + 1)]

    for _ in range(k):
        for i in range(1, n):
            people[i] += people[i - 1]

    return people[n - 1]

def main():
    T = int(input().strip())

    for _ in range(T):
        k = int(input().strip())
        n = int(input().strip())
        print(sol(k, n))

if __name__ == '__main__':
    main()