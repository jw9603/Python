def solution(strArr):
    return [strArr[i].lower() if i %2 == 0 else strArr[i].upper() for i in range(len(strArr))]

if __name__ == '__main__':
    print(solution((["AAA","BBB","CCC","DDD"])))
    print(solution(["aBc","AbC"]))