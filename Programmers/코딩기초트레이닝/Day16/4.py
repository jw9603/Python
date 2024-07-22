def solution(myString):
    return ''.join(['A' if myString[i].lower() == 'a' else myString[i].lower() for i in range(len(list(myString)))])

# "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환 이므로 myString[i].lower() == 'a' 에서 lower()가 들어가야 함.

##################### 다른 풀이 #####################
def solution(myString):
    return myString.lower().replace('a', 'A')
##################### 다른 풀이 #####################


if __name__ == '__main__':
    print(solution("abstract algebra"))
    print(solution("PrOgRaMmErS"))