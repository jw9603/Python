def solution(todo_list, finished):
    return [todo_list[i] for i in range(len(todo_list)) if int(finished[i]) == 0]

if __name__ == '__main__':
    print(solution(["problemsolving", "practiceguitar", "swim", "studygraph"], ['true', 'false', 'true', 'false']))