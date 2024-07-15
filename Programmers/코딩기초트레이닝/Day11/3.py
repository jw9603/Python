def solution(my_string, indices):
    
    ans = ''
    for i in range(len(my_string)):
        if i not in indices:
            ans += my_string[i]
    return ans

if __name__ == '__main__':
    print(solution("apporoograpemmemprs",[1, 16, 6, 15, 0, 10, 11, 3]))