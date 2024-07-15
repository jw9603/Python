def solution(arr, idx):
    for i in range(len(arr)):
        if arr[i] == 1 and i >= idx:
            return i
        
    return -1

################### 다른 풀이 ###################
def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1

    return answer
# index 함수의 두번째 인자는 시작 인덱스이다. 즉 값 1의 index를 찾을 때 idx부터의 index를 찾으라는 뜻
################### 다른 풀이 ###################

if __name__ == '__main__':
    print(solution([0,0,0,1],1))
    print(solution([1, 0, 0, 1, 0, 0],4))
    print(solution[1, 1, 1, 1, 0],3)