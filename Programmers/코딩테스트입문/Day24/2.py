# https://school.programmers.co.kr/learn/courses/30/lessons/120885
# 이진수 더하기
def solution(bin1, bin2):
    return bin(int(bin1,2)+int(bin2,2)).replace('0b',"")

if __name__ == '__main__':
    print(solution("10","11"))
    print(solution("1001","1111"))
    

# int함수의 2번째 인자를 활용하여, 2, 8, 16진수 문자열을 정수형 (int)숫자로 형변환할 수 있다.

# 8진수 문자열을 정수형으로 변환: int("0o12",8)
# 16진수 문자열을 정수형으로 변환: int("0xa",16)
# 2진수 문자열을 정수형으로 변환: int("0b1010",2)
# oct(): 10진수 -> 8진수
# hex(): 10진수 -> 16진수
# bin(): 10진수 -> 2진수