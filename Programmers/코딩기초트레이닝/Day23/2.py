# https://school.programmers.co.kr/learn/courses/30/lessons/181841
# 꼬리 문자열
def solution(str_list, ex):
    return ''.join([i for i in str_list if ex not in i])

if __name__ == '__main__':
    print(solution(["abc", "def", "ghi"],"ef"))
    print(solution(["abc", "bbc", "cbc"],"c"))