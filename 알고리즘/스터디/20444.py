# 백준 20444. 색종이와 가위
# https://www.acmicpc.net/problem/20444
############################ 문제 이해 ############################
# 색종이를 자를 때는 다음과 같은 규칙을 따른다.
    # 1. 색종이를 자를 때는 한 변에 평행하게 자른다.
    # 2. 자르기 시작했으면, 경로 상의 모든 색종이를 자를 때까지 멈추지 않는다.
    # 3. 이미 자른 곳을 또 자를 수 없다.
# n번의 가위질로 k개의 색종이 조각을 만들수 있다면 'YES', 아니면 'NO'

# n번 자르는 행위는 가로, 세로가 있다. 가로로 자른 횟수 + 세로로 자른 횟수 == n
# 종이 개수 == (가로로 자른 횟수 + 1) * (세로로 자른 횟수 + 1)
# 그런데 n과 k의 범위가 매우매우 크다. 즉, 이진 탐색을 통해 찾자!
############################ 문제 이해 ############################
def can_paper_cut(n, k):
    left, right = 0, n

    while left <= right:
        mid = (left + right) // 2
        cnt = (mid + 1) * (n - mid + 1)
        if cnt == k:
            return 'YES'
        elif cnt < k:
            left = mid + 1
        elif cnt > k:
            right = mid - 1
    
    return 'NO'
        
def main():
    n, k = map(int, input().split())
    print(can_paper_cut(n, k))

if __name__ == '__main__':
    main()
