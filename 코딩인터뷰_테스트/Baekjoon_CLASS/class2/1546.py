# 백준 1546. 평균
# https://www.acmicpc.net/problem/1546
################################### 문제 이해 ###################################
# 점수를 조작해서 집에 가져가기로 했다.
# 최댓값 == M, 모든 점수를 점수 / M * 100으로 고쳤다.
################################### 문제 이해 ###################################
def sol(N, scores):
    max_score = max(scores)
    res = [score / max_score * 100 for score in scores]

    return sum(res) / N
    
def main():
    N = int(input().strip())
    scores = list(map(int, input().split()))

    print(sol(N, scores))

if __name__ == '__main__':
    main()