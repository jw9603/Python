def solution(s):
    answer = 0
    s = list(s.split(' '))
    for i in range(len(s)):
        if s[i] == 'Z':
            answer -= int(s[i-1])
        else:
            answer += int(s[i])
    return answer

if __name__ == '__main__':
    print(solution("1 2 Z 3"))
    print(solution("10 20 30 40"))
    print(solution("10 Z 20 Z 1"))
    print(solution("10 Z 20 Z"))
    print(solution("-1 -2 -3 Z"))