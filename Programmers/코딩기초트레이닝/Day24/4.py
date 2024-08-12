# https://school.programmers.co.kr/learn/courses/30/lessons/181834
# l로 만들기

def solution(myString):
    return''.join(i.replace(i,"l") if i < "l" else i for i in myString)

if __name__ == '__main__':
    print(solution("abcdevwxyz"))
    print(solution("jjnnllkkmm"))