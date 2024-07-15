def solution(numbers):
    return sorted(numbers)[-1] * sorted(numbers)[-2]

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5]))
    print(solution([0, 31, 24, 10, 1, 9]))