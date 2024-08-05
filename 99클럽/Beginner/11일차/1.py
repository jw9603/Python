# 정수 내림차순으로 배치하기

def solution(n):
    return int(''.join(sorted(str(n),reverse=True)))

if __name__ == '__main__':
    print(solution(118372))