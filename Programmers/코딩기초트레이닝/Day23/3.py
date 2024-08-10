# https://school.programmers.co.kr/learn/courses/30/lessons/181840
# 정수 찾기
def solution(num_list, n):
    
    return int(n in num_list)

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5], 3))
    print(solution([15, 98, 23, 2, 15], 20))