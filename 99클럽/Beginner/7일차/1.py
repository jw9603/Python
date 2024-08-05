def solution(arr):
    ans = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            ans.append(arr[i])
            
    return ans

# def solution(arr):
#     # stack은 LIFO
    
#     stack = []
    
#     for num in arr:
#         if not stack or stack[-1] != num:
#             stack.append(num)
#     return stack

if __name__ == '__main__':
    print(solution([1,1,3,3,0,1,1]))
    print(solution([4,4,4,3,3]))