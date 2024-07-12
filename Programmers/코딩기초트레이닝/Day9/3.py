def solution(my_string, n):
   
    return my_string[len(my_string)-n:]

if __name__ =='__main__':
    print(solution("ProgrammerS123",11))
    print(solution("He110W0r1d",5))