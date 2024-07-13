def solution(my_string, m, c):
    return my_string[c-1::m]

if __name__ == '__main__':
    print(solution("ihrhbakrfpndopljhygc",4,2))
    print(solution("programmers",1,1))