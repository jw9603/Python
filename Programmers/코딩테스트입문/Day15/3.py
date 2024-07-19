def solution(s):
    answer = []
    for i in s:
        if s.count(i) > 1:
            continue
        answer.append(i)
    return ''.join(sorted(answer))

if __name__ == '__main__':
    print(solution("abcabcadc"))
    print(solution("abcd"))
    print(solution("hello"))