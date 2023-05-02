def solution(s):
    answer = []
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            answer.append(ord(s[i]))
    answer = sorted(answer)
    ans = ''
    for i in range(len(answer)):
        ans += chr(answer[i])
    return ans

if __name__ =='__main__':
    print(solution("abdc"))