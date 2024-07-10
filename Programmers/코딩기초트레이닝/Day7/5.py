def solution(arr):
    stk = []
    i = 0
    for i in range(len(arr)):
        while stk and stk[-1] >= arr[i]: # 3번 조건
            stk.pop()
        stk.append(arr[i]) # 1, 2 번 조건
    
    return stk

if __name__ =='__main__':
    print(solution([1,4,2,5,3]))