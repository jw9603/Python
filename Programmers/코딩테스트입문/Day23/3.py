# https://school.programmers.co.kr/learn/courses/30/lessons/120956
# 옹알이 (1)
def solution(babbling):
    
    
    return sum([1 for b in babbling if b.replace('aya','!').replace('ye','!').replace('woo','!').replace('ma','!').replace('!','')==''])

if __name__ == '__main__':
    
    print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
    print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))