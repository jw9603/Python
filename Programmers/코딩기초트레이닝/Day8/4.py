def solution(number):

    return sum([int(i) for i in number]) % 9

if __name__ == '__main__':
    print(solution("123"))
    print(solution("78720646226947352489"))