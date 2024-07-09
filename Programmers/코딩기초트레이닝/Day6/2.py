def solution(n, control):
    n += control.count('w') - control.count('s') + 10 * control.count('d') - 10 * control.count('a')
    return n

if __name__ =='__main__':
    print(solution(0,"wsdawsdassw"))