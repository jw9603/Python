def solution(num1, num2):
    answer = 0
    if num1==num2:
        return 1
    else:
        return -1

if __name__ == "__main__":
    print(solution(1,2))
    print(solution(3,5))
    print(solution(4,4))