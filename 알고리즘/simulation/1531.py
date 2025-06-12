# 백준 1531. 투명
# https://www.acmicpc.net/problem/1531
############################## 문제 이해 ##############################
# 1 x 1 크기의 그림으로 모자이크한 100 x 100 크기의 그림을 가지고 있다.
# 모자이크 중 일부 그림이 너무 보기 싫어서 N개의 불투명한 종이로 그림을 가리기 시작했다.
# 불투명한 종이로 가린다고 항상 그 그림이 안 보이는 것은 아니다. 
# 그 그림의 현재 부분 위에 M개 이하의 종이가 올려져 있으면 그림은 그 부분에서 보이게 된다.

# 그림의 크기는 100 x 100이고, N개의 종이는 왼쪽 아래 모서리 좌표와 오른쪽 위 

# 입력:
# 첫째 줄에 N과 M, 둘째 줄부터 N개의 줄에 종이의 좌표

# 알고리즘
# 불투명한 종이 M개 초과로 올려져야 함
############################## 문제 이해 ##############################
def define_paper(N):
    paper = [[0] * 100 for _ in range(100)]

    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                paper[i - 1][j - 1]  += 1
    
    return paper

def cnt_picture(M, paper):
    cnt = 0

    for i in range(100):
        for j in range(100):
            if paper[i][j] > M:
                cnt += 1
    
    return cnt

def main():
    N, M = map(int, input().split())

    paper = define_paper(N)
    print(cnt_picture(M, paper))

if __name__ == '__main__':
    main()