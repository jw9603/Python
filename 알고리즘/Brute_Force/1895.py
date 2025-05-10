# 백준 1895. 필터
# https://www.acmicpc.net/problem/1895
################################### 문제 이해 ###################################
# 이미지 I는 R * C, 각 픽셀은 어두운 정도 V를 나타낸다.

################################### 문제 이해 ###################################
def median_filter(R, C, img, T):
    cnt = 0

    for i in range(1, R - 1):
        for j in range(1, C - 1):
            window = []
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    window.append(img[i + di][j + dj])

            window.sort()
            median = window[4]

            if median >= T:
                cnt += 1
    
    return cnt

def main():
    R, C = map(int, input().split())
    img = [list(map(int, input().split())) for _ in range(R)]
    T = int(input().strip())

    print(median_filter(R, C, img, T))

if __name__ == '__main__':
    main()