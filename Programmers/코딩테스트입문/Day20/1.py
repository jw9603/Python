def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    
    w = max(x) - min(x)
    h = max(y) - min(y)
    return w * h

if __name__ == '__main__':
    print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
    print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))