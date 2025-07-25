# 백준 14626. ISBN
# https://www.acmicpc.net/problem/14626
####################################### 문제 이해 #######################################
# ISBN은 전 세계 모든 도서에 부여된 고유번호로, 국제 표준 도서번호이다.
# 13자리의 숫자로 표시된다. 그 중 마지막 숫자는 체크기호로 ISBN의 정확성 여부를 점검할 수 있는 숫자이다.
# ISBN이 abcdefghijklm 일 때, a+3b+c+3d+e+3f+g+3h+i+3j+k+3l+m ≡ 0 (mod 10)
####################################### 문제 이해 #######################################
def sol(isbn):
    total = 0
    missing_index = -1
    weights = [1 if i % 2 == 0 else 3 for i in range(12)]

    for i in range(12):
        if isbn[i] == '*':
            missing_index = i
            continue
        total += int(isbn[i]) * weights[i]
    
    check_digit = int(isbn[12])
    for x in range(10):
        candidate_total = total + x * weights[missing_index]
        if (candidate_total + check_digit) % 10 == 0:
            return x
        
def main():
    isbn = input().strip()

    print(sol(isbn))

if __name__ == "__main__":
    main()