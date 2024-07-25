def solution(array, height):
    ans = 0
    for i in array:
        if i > height:
            ans += 1
    return ans

if __name__ == '__main__':
    print(solution([149, 180, 192, 170],187))
    print(solution([180, 120, 140],190))