def solution(my_string):
    return ''.join(sorted(my_string.lower()))

if __name__ == '__main__':
    print(solution("Bcad"))
    print(solution("heLLo"))
    print(solution("Python"))