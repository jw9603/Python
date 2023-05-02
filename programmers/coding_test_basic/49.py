def solution(s):
    s = list(s.split())
    answer = 0
    for i in range(len(s)):
        if s[i] == 'Z':
            answer -= int(s[i-1])
        else:
            answer += int(s[i])
    return answer

if __name__ =='__main__':
    print(solution("10 Z 20 Z 1"))