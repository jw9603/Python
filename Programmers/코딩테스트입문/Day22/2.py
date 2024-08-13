# https://school.programmers.co.kr/learn/courses/30/lessons/120875
# 평행

def solution(dots):
    a,b,c,d = dots
    
    if abs((a[0]-b[0]) / (a[1]-b[1])) == abs((c[0]-d[0]) / (c[1]-d[1])):
        return 1
    elif abs((a[0]-c[0]) / (a[1]-c[1])) == abs((b[0]-d[0]) / (b[1]-d[1])):
        return 1
    elif abs((a[0]-d[0]) / (a[1]-d[1])) == abs((c[0]-b[0]) / (c[1]-b[1])):
        return 1

    return 0

if __name__ == '__main__':
    print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
    print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))