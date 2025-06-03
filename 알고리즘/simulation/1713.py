# 백준 1713. 후보 추천하기
# https://www.acmicpc.net/problem/1713
############################### 문제 이해 ###############################
# 학생회장 후보는 일정 기간동안 전체 학생의 추천에 의하여 정해진 수만큼 선정된다.
# 추천받은 학생의 사진을 사진틀에 게시하고 추천받은 횟수를 표시하는 규칙은 다음과 같다.

# 1. 학생들이 추천받은 횟수를 시작하기 전에 모든 사진틀은 비어있다.
# 2. 어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시 되어야 한다.
# 3. 비어있는 사진틀이 없는 경우에는 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고,
# 그 자리에 새롭게 추천받은 학생의 사진을 게시한다.
# 이때 현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는 그러한 학생들 중 게시된 지
# 가장 오래된 사진을 삭제한다.
# 4. 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가
# 5. 사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.

# 후보의 수 즉, 사진틀의 개수와 전체 학생의 추천 결과가 추천받은 순서대로 주어졌을 때,
# 최종 후보가 누구인지 결정하는 프로그램 작성

# 입력
# 첫째 줄에는 사진틀의 개수 N, 둘째 줄에는 전체 학생의 총 추천 횟수가 주어진다.
# 셋째 줄에는 추천받은 학생을 나타내는 번호가 순서대로 주어진다.
# 추천 횟수는 1000번 이하, 학생을 나타내는 번호는 1이상 100이하의 자연수

# 출력: 사진틀에 사진이 게재된 최종 후보의 학생 번호를 증가하는 순서대로 출력

# 알고리즘
# 우선, 각각의 변수의 자료구조를 선택하자
# 1. 결과 변수: 리스트 
# 2. 
############################### 문제 이해 ###############################
# 1. 리스트로 구현
def sol(N, nums):
    result = []

    for num in nums: # nums: 추천받은 학생을 나타내는 번호
        # 1. 현재 추천 받은 학생의 사진이 걸려 있지 않다면?
        if num not in [x[0] for x in result]:
            # 1.1 사진틀에 공간이 있다.
            if len(result) < N:
                result.append([num, 1])
            # 1.2 모든 사진들이 꽉차있다면? -> 현재까지 추천 받은 횟수가 가장 적은 학생의 사진 삭제
            else:
                min_num = min(result, key=lambda x: x[1])
                result.remove(min_num)
                result.append([num, 1])
        # 2. 현재 추천 받은 학생의 사진이 걸려 있다면?
        else:
            for i in range(len(result)):
                if result[i][0] == num:
                    result[i][1] += 1
                    break
    
    return sorted([result[i][0] for i in range(len(result))])
            
def main():
    N = int(input().strip())
    M = int(input().strip())
    nums = list(map(int, input().split()))

    print(*sol(N, nums))

if __name__ == '__main__':
    main()

# 2. 딕셔너리로 구현
from collections import defaultdict
def sol(N, nums):
    # key: 후보자 번호, value: 추천 받은 수
    recommend_cnt = defaultdict(int)
    frame = [] # 사진틀: 학생 번호만 저장

    for num in nums: # nums: 추천받은 학생을 나타내는 번호
        # 1. 현재 추천 받은 학생의 사진이 걸려 있지 않다면?
        if num not in frame:
            # 1.1 사진틀에 공간이 있다.
            if len(recommend_cnt) < N:
                frame.append(num)
                recommend_cnt[num] += 1
            # 1.2 모든 사진들이 꽉차있다면? -> 현재까지 추천 받은 횟수가 가장 적은 학생의 사진 삭제
            else:
                min_vote = min([recommend_cnt[x] for x in frame])
                for f in frame:
                    if recommend_cnt[f] == min_vote:
                        frame.remove(f)
                        del recommend_cnt[f]
                        break
                frame.append(num)
                recommend_cnt[num] += 1
        # 2. 현재 추천 받은 학생의 사진이 걸려 있다면?
        else:
            recommend_cnt[num] += 1
    
    return sorted(frame)
            
def main():
    N = int(input().strip())
    M = int(input().strip())
    nums = list(map(int, input().split()))

    print(*sol(N, nums))

if __name__ == '__main__':
    main()