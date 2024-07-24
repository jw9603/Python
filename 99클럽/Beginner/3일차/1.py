# 문자열 내 p와 y의 개수
def solution(s):
    return bool(1) if s.lower().count('p') == s.lower().count('y') else bool(0)

if __name__ == '__main__':
    print(solution("pPoooyY"))
    print(solution("Pyy"))