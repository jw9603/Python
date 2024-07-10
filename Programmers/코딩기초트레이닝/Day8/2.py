def solution(a, b, c, d):
    dice = [a,b,c,d]
    if len(set(dice)) == 1: # case1
        return dice[0] * 1111
    elif len(set(dice)) == 2:
        dice1 = sorted(dice)
        if dice1[1] != dice1[2]: # case 3
            return (dice1[1]+dice1[2]) * abs(dice1[1]-dice1[2])
        else: # case2
            if dice1[1] > dice1[0]: # p > q
                return (10*dice1[1] + dice1[0])**2
            else: # p < q
                return (10*dice1[0] +  dice1[-1])**2
    elif len(set(dice)) == 3: # case 4
        dice1 = sorted(dice)
        case4 = []
        for i in range(len(dice1)-1):
            if dice1[i] == dice1[i+1]:
                case4.append(dice1[i])
        return (list(set(dice) - set(case4)))[0] * (list(set(dice) - set(case4)))[1]
    else:
        return sorted(dice)[0]
            
if __name__ == '__main__':
    print(solution(2,2,2,2))
    print(solution(4,1,4,1))
    print(solution(6,3,3,6))
    print(solution(2,5,2,6))
    print(solution(6,4,2,5))
