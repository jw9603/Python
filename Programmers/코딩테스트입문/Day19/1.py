def solution(array):
    return ''.join(str(i) for i in array).count('7')

if __name__ == '__main__':
    print(solution([7,77,17]))
    print(solution([10,29]))