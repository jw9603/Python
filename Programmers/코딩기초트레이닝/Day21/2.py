def solution(rank, attendance):
    res = []
    for i in range(len(rank)):
        if attendance[i]:
            res.append((rank[i],i))

    res.sort(key= lambda v: v[0])
            
    return 10000 * res[0][1] + 100 * res[1][1] + res[2][1]

if __name__ == '__main__':
    print(solution([3, 7, 2, 5, 4, 6, 1],[0, 1, 1, 1, 1, 0, 0]))
    print(solution([1,2,3],[1,1,1]))
    print(solution([6, 1, 5, 2, 3, 4],[1, 0, 1, 0, 0, 1]))