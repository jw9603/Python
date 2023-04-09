def solution(box, n):
    
    return (box[0] // n) * (box[1] // n) * (box[2] // n)

if __name__ =='__main__':
    print(solution([10, 8, 6],3))