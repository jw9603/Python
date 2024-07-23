def solution(myString, pat):
    
    index = myString.find(pat)
    cnt = 0
    while index != -1:
        cnt += 1
        index = myString.find(pat,index+1)
    return cnt

if __name__ == '__main__':
    print(solution("banana","ana"))
    print(solution("aaaa","aa"))