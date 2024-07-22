# 자연수 뒤집어 배열로 만들기
def solution(n):
    return[int(i) for i in str(n)[::-1]]

if __name__ == '__main__':
    print(solution(12345))