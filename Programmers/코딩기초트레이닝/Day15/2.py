def solution(arr):
    
    x = 0
    while True:
        answer = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                answer.append(i/2)
            elif i < 50 and i % 2 == 1:
                answer.append(i*2 + 1)
            else:
                answer.append(i)

        if answer == arr:
            return x
        else:
            x += 1
            arr = answer
            
if __name__ == '__main__':
    print(solution([1,2,3,100,99,98]))