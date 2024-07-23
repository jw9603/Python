def solution(strArr):
    return [i for i in strArr if "ad" not in i]

if __name__ == '__main__':
    print(solution(["and","notad","abcd"]))
    print(solution(["there","are","no","a","ds"]))