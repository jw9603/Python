# https://school.programmers.co.kr/learn/courses/30/lessons/120887
# k의 개수

# def solution(i, j, k):
#     answer = 0
#     for i in range(i,j+1):
#         for w in str(i):
#             if w == str(k):
#                 answer += 1
#     return answer

########## 다른 풀이 #############
def solution(i, j, k):
    
    return sum([str(i).count((str(k))) for i in range(i,j+1)])
########## 다른 풀이 #############

if __name__ == '__main__':
    print(solution(1,13,1))
    print(solution(10,50,5))
    print(solution(3,10,2))