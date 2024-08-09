def solution(num_str):
    return sum([int(i) for i in num_str])

if __name__ == '__main__':
    print(solution("123456789"))
    print(solution("1000000"))