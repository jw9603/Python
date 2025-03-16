# 프로그래머스 - 두 큐 합 같게 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/118667
from collections import deque
def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum_q1, sum_q2 = sum(q1), sum(q2)

    target = (sum_q1 + sum_q2) // 2
    total_len = len(q1) + len(q2)

    cnt = 0
    while sum_q1 != target:

        if sum_q1 > sum_q2:
            val = q1.popleft()
            sum_q1 -= val
            q2.append(val)
            sum_q2 += val
        elif sum_q1 < sum_q2:
            val = q2.popleft()
            sum_q2 -= val
            q1.append(val)
            sum_q1 += val
        else:
            return cnt
        cnt += 1

        if cnt > total_len * 2:
            return -1
    return cnt

if __name__ == '__main__':
    queue1, queue2 = [3, 2, 7, 2], [4, 6, 5, 1]
    print(solution(queue1=queue1, queue2=queue2))