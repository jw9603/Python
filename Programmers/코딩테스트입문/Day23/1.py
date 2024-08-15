# https://school.programmers.co.kr/learn/courses/30/lessons/120880
# 특이한 정렬 
def solution(numlist, n):
    return sorted(numlist,key=lambda x : (abs(x-n),n-x))

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5, 6],4))
    print(solution([10000,20,36,47,40,6,10,7000],30))