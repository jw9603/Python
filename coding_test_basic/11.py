import collections

def solution(array):
    cnt = collections.Counter(array)
    most_common = cnt.most_common()
    
    if len(most_common)== 1 or most_common[0][0] != most_common[1][0]:
        return most_common[0][0]
    else:
        return -1
    
if __name__ == '__main__':
    print(solution([1, 2, 3, 3, 3, 4]))
    # solution([1, 2, 3, 3, 3, 4])