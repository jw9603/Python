def solution(arr, queries):
    answer = []
    for i in queries:
        a = arr[i[0]:i[1]+1] # a = [0,1,2,4,3], i = [0,4,2]
        a.sort() # [0,1,2,3,4]
        for j in a: 
            if j > i[2]: # j = ,i[2] = 2
                answer.append(j)
                break
            elif j == a[-1]:
                answer.append(-1)
    return answer

if __name__ == '__main__':
    print(solution([0, 1, 2, 4, 3], [[0, 4, 2],[0, 3, 2],[0, 2, 2]]))