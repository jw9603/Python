def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        ans = 1
        for i in num_list:
            ans *= i
        return ans

if __name__ == '__main__':
    print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
    print(solution([2, 3, 4, 5]))