def solution(arr, queries):
    for element in queries:
        for i in range(element[0],element[1]+1):
            arr[i] += 1
        
    return arr
#################### 다른 풀이 ####################
def solution(arr, queries):
    for s,e in queries:
        for i in range(s,e+1):
            arr[i] += 1
        
    return arr
#################### 다른 풀이 ####################

if __name__ == '__main__':
    print(solution([0,1,2,3,4],[[0, 1],[1, 2],[2, 3]]))