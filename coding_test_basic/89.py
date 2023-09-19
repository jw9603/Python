def solution(numlist, n):

    return sorted(numlist,key = lambda x : (abs(x-n),-x))

if __name__ =='__main__':
    
    print(solution([10000,20,36,47,40,6,10,7000],30))