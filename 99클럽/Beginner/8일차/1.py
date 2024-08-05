def solution(s):
    ans = []
    for i in s:
        if i == '(':
            ans.append(i)
        else: # i == ')'
            if not ans: # ans가 비어있다면?
                return False 
            else: # ans가 비어있지 않다면?
                ans.pop()
    return True if not ans else False

if __name__ == '__main__':
    print(solution("()()"))
    print(solution("(())()"))
    print(solution(")()("))
    print(solution("(()("))