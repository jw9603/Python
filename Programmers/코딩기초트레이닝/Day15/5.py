def solution(myString, pat):
    return 1 if pat.lower() in myString.lower() else 0

if __name__ == '__main__':
    print(solution("AbCdEfG","aBc"))
    print(solution("aaAA","aaaaa"))