def solution(my_string):
    return sorted([int(i) for i in my_string if i.isnumeric()])

if __name__ == '__main__':
    print(solution("hi12392"))
    print(solution("p2o4i8gj2"))
    print(solution("abcde0"))