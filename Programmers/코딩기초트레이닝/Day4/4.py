def solution(ineq,eq,n,m):
    
    return int(eval(str(n)+ineq+eq.replace('!','')+str(m)))

if __name__ =='__main__':
    print(solution('<',"=",20,50))
    print(solution('>','!',41,78))