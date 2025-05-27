# 백준 1244. 스위치 켜고 끄기
# https://www.acmicpc.net/problem/1244
################################ 문제 이해 ################################
# 1부터 연속적으로 번호: 스위치
# 스위치는 켜져 있거나 꺼져있는 상태 -> 1: on, 0: off
# 학생 몇 명에게 자연수를 하나씩 나누어줌, 학생들은 자신의 성별과 받은 수에 따라 다른 방식으로 스위치를 조작

# 남학생: 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
# 여학생: 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를
# 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다. 구간에 속한 스위치 개수는
# 항상 홀수

# 입력
# 첫째 줄에는 스위치의 개수
# 둘째 줄에는 각 스위치의 상태가 주어진다. (1: on, 0: off)
# 셋째 줄에는 학생수가 주어진다.
# 넷째 줄부터 마지막 줄까지 한 줄에 한 학생의 성별, 학생이 받은 수가 주어진다. (남: 1, 여: 2)

# 출력:
# 스위치의 상태를 1번부터 마지막 스위치까지 한 줄에 20개씩 출력

# 알고리즘

################################ 문제 이해 ################################
def change_num(num):
    global switch
    if switch[num] == 1:
        switch[num] = 0
    else:
        switch[num] = 1

def simulate(n, sex, num):
    global switch
    # 남자: 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
    if sex == 1:
        for i in range(num, n + 1, num):
            change_num(i)
    # 여자
    else:
        # 받은 번호는 무조건 바꾼다.
        change_num(num)
        for i in range(n // 2):
            if num + i > n or num - i < 1:
                break
            if switch[num + i] == switch[num - i]:
                change_num(num + i)
                change_num(num - i)
            else:
                break
    
def print_result(n):
    global switch
    for i in range(1, n + 1):
        print(switch[i], end=' ')
        if i % 20 == 0:
            print()
    
def main():
    global switch
    # 입력
    n = int(input().strip()) # 스위치의 개수
    switch = [-1] + list(map(int, input().split())) # 1: on, 0: off
    students = int(input().strip()) # 학생수

    for _ in range(students):
        sex, num = map(int, input().split())

        # 1. 남학생, 여학생이 받은 수를 기반으로 스위치 조작
        simulate(n, sex, num)
    # 2. 결과 출력
    print_result(n)

if __name__ == '__main__':
    main()