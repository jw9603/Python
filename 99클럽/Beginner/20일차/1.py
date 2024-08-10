def solution(n, lost, reserve):
    
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
            
    return n- len(lost_set)


if __name__ == '__main__':
    print(solution(5,[2,4],[1,3,5]))
    print(solution(5,[2,4],[1,3,5]))
    print(solution(3,[3],[1]))