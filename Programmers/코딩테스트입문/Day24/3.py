# https://school.programmers.co.kr/learn/courses/30/lessons/120886
# A로 B만들기
def solution(before, after):
    # before의 순서를 바꾸어 after를 만들 수 있다면 1, 여기서 중요한게 순서를 바꾸는게 뒤집는것만 있는것이 아님
    return int(sorted(before) == sorted(after))

if __name__ == '__main__':
    print(solution("olleh","hello"))
    print(solution("allpe","apple"))