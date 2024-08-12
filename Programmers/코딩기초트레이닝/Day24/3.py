# https://school.programmers.co.kr/learn/courses/30/lessons/181835
# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    return [i * k if k % 2!= 0 else i + k for i in arr]

if __name__ == '__main__':
    print(solution([1, 2, 3, 100, 99, 98],3))
    print(solution([1, 2, 3, 100, 99, 98],2))