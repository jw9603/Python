# https://school.programmers.co.kr/learn/courses/30/lessons/181838
# 날짜 비교하기

def solution(date1, date2):
    
    return int(int(''.join(map(str,date1))) < int(''.join(map(str,date2))))

########## 다른 풀이 ############
def solution(date1,date2):
    
    return int(date1<date2) # 리스트끼리 비교 연산자를 진행하면, 각 요소 별로 진행해서 모두 만족하면 True, 하나라도 틀리면 False return

if __name__ == '__main__':
    print(solution([2021, 12, 28], [2021, 12, 29]))
    print(solution([1024, 10, 24],[1024,10,24]))