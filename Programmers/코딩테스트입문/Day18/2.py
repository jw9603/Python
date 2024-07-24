def solution(n):

    return 1 if (n ** 0.5) %1 == 0 else 2

if __name__ == '__main__':
    print(solution(144))
    print(solution(976))