def solution(my_string):
    return my_string.split()
# split() 메서드는 기본적으로 연속된 공백을 하나의 구분자로 인식하여 문자열을 나눈다.
if __name__ == '__main__':
    print(solution(" i    love  you"))
    print(solution("    programmers  "))