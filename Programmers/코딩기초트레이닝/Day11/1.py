def solution(my_string):
    return [my_string.count(i) for i in 'abcdefghijklmnopqrstuvwxyz'.upper() + 'abcdefghijklmnopqrstuvwxyz']

if __name__ == '__main__':
    print(solution("Programmers"))