# https://school.programmers.co.kr/learn/courses/30/lessons/120876
# 겹치는 선분의 길이
def solution(lines):
    
    ans = [set(range(min(l),max(l))) for l in lines]
    
    return len(ans[0] & ans[1] | ans[0] & ans[2] | ans[1] & ans[2])

if __name__ == '__main__':
    print(solution([[0, 1], [2, 5], [3, 9]]))
    print(solution([[-1, 1], [1, 3], [3, 9]]))
    print(solution([[0, 5], [3, 9], [1, 10]]))