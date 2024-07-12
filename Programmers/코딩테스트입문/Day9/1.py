def solution(hp):
    return hp // 5 + hp % 5 // 3 + hp % 5 % 3 // 1

if __name__ == '__main__':
    print(solution(23))
    print(solution(24))
    print(solution(999))