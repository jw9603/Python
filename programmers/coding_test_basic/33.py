def solution(hp):
    
    return hp // 5 + (hp % 5) // 3 + hp % 5 % 3 

if __name__ =='__main__':
    print(solution(345))