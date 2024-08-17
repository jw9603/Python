# https://school.programmers.co.kr/learn/courses/30/lessons/120921
# 문자열 밀기
def solution(A, B):
    for i in range(len(A)):
        if A == B:
            return i
        A = A[-1] + A[:-1]
    return -1

if __name__ == '__main__':
    print(solution("hello","ohell"))
    print(solution("apple","elppa"))
    print(solution("atat","tata"))
    print(solution("abc","abc"))