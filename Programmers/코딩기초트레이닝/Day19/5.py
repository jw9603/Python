def solution(arr, k):
    # 집합 자료형은 자동적으로 오름차순으로 정렬되므로 위 문제에는 적합하지 않음
    ans = []
    
    for i in arr:
        if i not in ans:
            ans.append(i)
        if len(ans) == k:
            break
            
    return ans + [-1] *(k-len(ans))

if __name__ == '__main__':
    print(solution([0, 1, 1, 2, 2, 3],3))
    print(solution([0, 1, 1, 1, 1],4))