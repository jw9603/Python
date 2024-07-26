def solution(strArr):
    
    ans = [len(i) for i in strArr] # 각 요소들의 길이들이 들어있는 배열
    tmp = []

    for i in set(ans):
        tmp.append(ans.count(i))
    return max(tmp)

if __name__ == '__main__':
    print(solution(["a","bc","d","efg","hi"]))