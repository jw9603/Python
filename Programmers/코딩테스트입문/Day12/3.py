def solution(my_string):
    return sum([int(i) for i in my_string if i.isnumeric()])

if __name__ == '__main__':
    print(solution("aAb1B2cC34oOp"))
    print(solution("1a2b3c4d123"))