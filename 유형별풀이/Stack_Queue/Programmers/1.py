# 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

################### 스택을 활용한 풀이 ###############
# from collections import deque
# def solution(arr):
#     stack = deque()

#     for num in arr:
#         if not stack or stack[-1] != num: 
#             stack.append(num)
#     return list(stack)
################### 스택을 활용한 풀이 ###############


########### 반복문에서 비교를 활용한 풀이 ##############
def solution(arr):
    result = [arr[0]]
    
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])
    return result
########### 반복문에서 비교를 활용한 풀이 ##############



if __name__ == '__main__':
    print(solution([1,1,3,3,0,1,1]))
    print(solution([4,4,4,3,3]))
    