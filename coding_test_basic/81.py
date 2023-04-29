def solution(my_string):
    my_string = ''.join([word if word.isnumeric() else ' ' for word in list(my_string)])

    return sum(list(map(int,my_string.split())))

if __name__ == '__main__':
    print(solution("aAb1B2cC34oOp"))