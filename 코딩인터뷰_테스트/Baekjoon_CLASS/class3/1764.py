# 백준 1764. 듣보잡
# https://www.acmicpc.net/problem/1764
################################### 문제 이해 ###################################
# 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램 작성

# 입력:
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어집니다.
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N + 2번째 줄부터 보도 못한 사람의 이름
# 이 순서대로 주어진다.
# 출력: 듣보잡의 수와 그 명단을 사전순으로 출력

# 알고리즘:
# 1. 집합 자료형을 사용!
# 2. 그 다음 and 연산자 사용
# 3. 정렬하기
################################### 문제 이해 ###################################
def sol(no_listen, no_seen):
    return len(set(no_listen) & set(no_seen)), *sorted(list(set(no_listen) & set(no_seen)))

def main():
    N, M = map(int, input().split())
    no_listen = [input().strip() for _ in range(N)]
    no_seen = [input().strip() for _ in range(M)]
    
    print(*sol(no_listen, no_seen), sep='\n')

if __name__ == '__main__':
    main()