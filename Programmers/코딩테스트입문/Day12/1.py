def solution(my_string):
    return ''.join([i for i in my_string if not (i in 'aeiou')])

if __name__ == '__main__':
    print(solution("bus"))
    print(solution("nice to meet you"))