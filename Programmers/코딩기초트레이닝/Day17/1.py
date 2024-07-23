def solution(myString, pat):
    return myString[:myString.rfind(pat)+len(pat)]


# rfind 함수에 대해 알아보자
'''
문자열 내부에서 특정 문자가 어디에 위치하는지 찾을 때 사용한다.
find 함수는 왼쪽부터 찾고, rfind함수는 오른쪽부터 찾는다. == 지정 문자열 끝 위치라 할 수 있다.

string.rfind(value,start,end)
예를들어, string.rfind(value,start) 는 가능, string.rfind(value,end)는 불가능

'''

if __name__ == '__main__':
    print(solution("AbCdEFG","dE"))
    print(solution("AAAAaaaa","a"))