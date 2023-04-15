def solution(s1, s2):
    ans = len(set(s1) & set(s2))
    return ans

if __name__ =='__main__':
    print(solution(["a", "b", "c"]	,["com", "b", "d", "p", "c"]))