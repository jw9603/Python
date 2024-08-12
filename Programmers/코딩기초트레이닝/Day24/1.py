# https://school.programmers.co.kr/learn/courses/30/lessons/181837
# 커피 심부름
def solution(order):
    answer = 0
    
    for i in order:
        if 'americano' in i:
            answer += 4500
        elif 'cafelatte' in i:
            answer += 5000
        else:
            answer += 4500
    return answer

if __name__ == '__main__':
    print(solution(["cafelatte", "americanoice", "hotcafelatte", "anything"]))
    print(solution(["americanoice", "americano", "iceamericano"]))