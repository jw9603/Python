def solution(my_string, is_prefix):
    return 1 if my_string.startswith(is_prefix) else 0

if __name__ == '__main__':
    print(solution("banana","ban"))
    print(solution("banana","nan"))
    print(solution("banana","abcd"))
    print(solution("banana","bananan"))