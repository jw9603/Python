# 문자열을 정수로 바꾸기

def solution(s):
    # return int(s) if '-' not in s else int(s[0] + s[1:])
    return int(s)

if __name__ == '__main__':
    print(solution('1234'))
    print(solution('-1234'))