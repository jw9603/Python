def solution(array, n):
    array.sort()
    ans = []
    for i in range(len(array)):
        ans.append(abs(n-array[i]))
    # print(ans)
    return array[ans.index(min(ans))]

if __name__ == '__main__':
    print(solution([10, 11, 12],13))