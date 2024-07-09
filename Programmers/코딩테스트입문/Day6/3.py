def solution(numLog):
    ans = ''
    for i in range(1,len(numLog)):
        if numLog[i] - numLog[i-1] == 1:
            ans += 'w'
        elif numLog[i] - numLog[i-1] == -1:
            ans += 's'
        elif numLog[i] - numLog[i-1] == 10:
            ans += 'd'
        elif numLog[i] - numLog[i-1] == -10:
            ans += 'a'
    return ans

if __name__ =='__main__':
    print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))