def solution(sides):
    sides.sort()
    
    return 1 if sides[-1] < sides[0] + sides[1] else 2

if __name__ == '__main__':
    print(solution([199, 72, 222]))