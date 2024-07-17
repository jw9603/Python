def solution(sides):
    return 1 if sorted(sides)[-1] < sorted(sides)[0] + sorted(sides)[1] else 2

if __name__ == '__main__':
    print(solution([1,2,3]))
    print(solution([3,6,2]))
    print(solution([199,72,222]))