def solution(numbers):
    answer = ''
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for id,num in enumerate(num):
        numbers = numbers.replace(num,str(id))
   
    return int(numbers)

if __name__ =='__main__':
    print(solution("onetwothreefourfivesixseveneightnine"))