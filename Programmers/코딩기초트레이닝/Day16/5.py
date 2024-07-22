def solution(my_string, alp):
    return my_string.lower().replace(alp,alp.upper())

if __name__ == '__main__':
    print(solution("programmers","p"))
    print(solution("lowercase","x"))