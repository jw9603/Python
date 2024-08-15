# https://school.programmers.co.kr/learn/courses/30/lessons/120882
# 등수 매기기
def solution(score):
    
    scores = [sum(i)/2 for i in score]
    sorted_score = sorted(scores,reverse=True)
    
    ans = []
    
    for i in scores:
        ans.append(sorted_score.index(i)+1)
    return ans

if __name__ == '__main__':
    print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
    print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))