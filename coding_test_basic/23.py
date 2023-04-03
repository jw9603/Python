def solution(num_list):
    cnt = 0
    cnt1 = 0
    for i in range(len(num_list)):
        
        if num_list[i] %2 == 0:
            cnt +=1
        else:
            cnt1 +=1
    return [cnt,cnt1]

# 다른 사람 문제 풀이

def solution1(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer

if __name__ =='__main__':
    print(solution([1,2,3,4,5]))
    print(solution1([1,2,3,4,5]))