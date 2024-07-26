def solution(numbers):
    return max(sorted(numbers)[-1]*sorted(numbers)[-2],sorted(numbers)[0]*sorted(numbers)[1])

if __name__ == '__main__':
    print(solution([1, 2, -3, 4, -5]))
    print(solution([0, -31, 24, 10, 1, 9]))
    print(solution([10, 20, 30, 5, 5, 20, 5]))