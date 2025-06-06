# 백준 17952. 과제는 끝나지 않아!
# https://www.acmicpc.net/problem/17952
################################ 문제 이해 ################################
# 거의 매일 과제를 하면서 보내고 있다.
# 그런데도 과제가 줄어들 기미가 보이지 않는데, 바로 분단위로 과제가 추가되고 있기 때문이다.
# 아래와 같은 규칙으로 과제를 해 나가고 있다.

# 1. 과제를 가장 최근에 나온 순서대로 한다. 또한 과제를 받으면 바로 시작한다. -> LIFO
# 2. 과제를 하던 도중 새로운 과제가 나온다면, 하던 과제를 중단하고 새로운 과제를 진행.
# 3. 새로운 과제가 끝났으면, 이전에 하던 과제를 이전에 하던 부분부터 이어서 한다.

# 성애는 과제를 받자마자 이 과제가 몇 분이 걸릴지 정확하게 알 수 있고, 성애가 제출한 과제는 무조건
# 만점을 받는다.
# 성애는 이번 학기에 자기가 받을 과제 점수를 예상해보고 싶다.
# 성애가 받을 과제 점수를 계산해라.

# 입력
# 첫째 줄에 이번 학기가 몇 분인지를 나타내는 정수 N이 주어진다.
# 두 번째 줄부터 N줄 동안은 학기가 시작하고 N분째 주어진 과제의 정보가 아래의 두 경우 중 하나로 주어짐

# 1 A T: 과제의 만점은 A점이고, 성애가 이 과제를 해결하는 데 T 분이 걸린다. A와 T는 모두 정수
# 0: 해당 시점에는 과제가 주어지지 않았다.

# 출력: 성애가 받을 과제 점수를 출력

# 알고리즘

################################ 문제 이해 ################################
def calculate_assignment_score(N):
    score = 0
    stack = []

    for _ in range(N):
        assignment_info = list(map(int, input().split()))

        if assignment_info[0] == 0:
            if len(stack) != 0:
                a, t = stack.pop()

                if t == 1:
                    score += a
                else:
                    stack.append((a, t - 1))
 
        if assignment_info[0] == 1:
            a, t = assignment_info[1], assignment_info[2]

            if t == 1:
                score += a
            else:
                stack.append((a, t - 1))
    
    return score

def main():
    N = int(input().strip())
    print(calculate_assignment_score(N))

if __name__ == '__main__':
    main()