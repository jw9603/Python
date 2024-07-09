def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1]-num_list[-2])
        return num_list
    else:
        num_list.append(num_list[-1]*2)
        return num_list
    
if __name__ =='__main__':
    print(solution([2,1,6]))
    print(solution([5,2,1,7,5]))