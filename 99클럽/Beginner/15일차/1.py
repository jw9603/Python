def solution(answers): # len(answers) = 5
    num1 = [1,2,3,4,5] # len(num1) = 5
    num2 = [2,1,2,3,2,4,2,5] # len(num2) = 8
    num3 = [3,3,1,1,2,2,4,4,5,5] # len(num3) = 10
    score = [0,0,0]
    res = []
    
    for i, ans in enumerate(answers): # i = {0,1,2,3,4}
        if ans == num1[i%len(num1)]:
            score[0] += 1
        if ans == num2[i%len(num2)]:
            score[1] += 1
        if ans == num3[i%len(num3)]:
            score[2] += 1
    
    for i,s in enumerate(score):
        if s == max(score):
            res.append(i+1)
        
    return res

if __name__ == '__main__':
    print(solution([1,2,3,4,5]))
    print(solution([1,3,2,4,2]))