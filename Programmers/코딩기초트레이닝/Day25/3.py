# https://school.programmers.co.kr/learn/courses/30/lessons/181830
# 정사각형으로 만들기
def solution(arr):    
    w = len(arr)
    h = len(arr[0])
    
    if w > h:
        for i in range(len(arr)):
            for j in range(w-h):
                arr[i].append(0)
    else:
        for _ in range(h-w):
            arr.append([0] * len(arr[0]))
            
        
    return arr

if __name__ == '__main__':
    print(solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]))
    print(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))
    print(solution([[1, 2], [3, 4]]))