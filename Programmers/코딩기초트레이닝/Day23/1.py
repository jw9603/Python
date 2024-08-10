# 부분 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181842

def solution(str1, str2):
    
    return int(str1 in str2)

if __name__ == '__main__':
    print(solution("abc","aabcc"))
    print(solution("tbt","tbbttb"))