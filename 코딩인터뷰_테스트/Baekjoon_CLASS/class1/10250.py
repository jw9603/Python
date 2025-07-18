# 백준 10250. ACM 호텔
# https://www.acmicpc.net/problem/10250
############################### 알고리즘 풀이 ###############################
# 손님이 도착하는 대로 빈 방을 배정하고 있다.
# 손님들은 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호한다고 한다.
# 즉, 설문조사 결과 대로 호텔 정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램을 작성하고자 한다.

# W개의 방이 있는 H층의 건물, 호텔 정문은 일층 엘리베이터 바로 앞에 있다.
# 정문에서 엘리베이터까지의 거리는 무시, 모든 인접한 두 방사이의 거리는 같은 거리(거리 1)라고 가정

# 손님은 엘리베이터를 타고 이동하는 거리는 신경 안씀
# 걷는 거리가 같을 때에는 아래층의 방을 더 선호
# 결국 몇층이냐보다 엘리베이터로부터 얼마나 떨어

# 1등 : 101, 2등 : 201, 3등 : 301, 4등 : 401, 5등 : 501, 6등 : 601,,
# 즉 높이 만큼 먼저 정해져야함.
# 그 다음은 밑에층부터,,! 
# 7등 : 102 == (7 % 6, 7 // 6 + 1)
############################### 알고리즘 풀이 ###############################
def sol(H, N):
    floor = N % H
    room_line = N // H + 1

    if floor == 0:
        floor = H
        room_line -= 1
    
    return floor * 100 + room_line

def main():
    T = int(input().strip())

    for _ in range(T):
        H, W, N = map(int, input().split())
        print(sol(H, N))

if __name__ == '__main__':
    main()