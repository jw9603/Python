def gradient(a,b):
    return (a[1]-b[1])/(a[0]-b[0])
def solution(dots):
    if gradient(dots[0],dots[1]) == gradient(dots[2],dots[3]) or gradient(dots[0],dots[2]) == gradient(dots[1],dots[3]) or gradient(dots[0],dots[3]) == gradient(dots[1],dots[2]):
        return 1
    return 0

if __name__ == '__main__':
    print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))
    print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))