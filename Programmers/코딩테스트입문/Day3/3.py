from collections import Counter
def solution(array):
    res = Counter(array).most_common(2)
    if len(res) == 1:
        return res[0][0]
    elif res[0][1] > res[1][1]:
        return res[0][0]
    else:
        return -1
    
if __name__ =='__main__':
    print(solution([1, 2, 3, 3, 3, 4]))
    print(solution([1, 1, 2, 2]))
    print(solution([1]))