def solution(arr):
    return sum(arr)/len(arr)


########### 다른 풀이 ##############
import numpy as np
def solution(arr):
    return np.array(arr).mean()
########### 다른 풀이 ##############

if __name__ == '__main__':
    print(solution([1,2,3,4]))
    print(solution([5,5]))