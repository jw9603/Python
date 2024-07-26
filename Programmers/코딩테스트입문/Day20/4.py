def solution(polynomial):
    answer = ''
    num = 0
    sum = 0
    polynomial = polynomial.replace(' ','').split('+')
    for i in polynomial:
        if i[-1] == 'x':
            num += 1 if len(i) == 1 else int(i[:-1])
        else:
            sum += int(i)

    if num > 0:
        answer = (str(num) if num > 1 else '')+ 'x' + (' + ' if sum >0 else '')
    answer += str(sum) if sum >0 else ""            
    return answer

if __name__ == '__main__':
    print(solution("3x + 7 + x"))
    print(solution("x + x + x"))