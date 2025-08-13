from stack import Stack
def is_valid(expression):
    stack = Stack()
    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            top = stack.pop()
            if (top == '(' and char != ')') or (top == '[' and char != ']') or (top == '{' and char != '}'):
                return False
    return stack.is_empty()

def is_valid_postfix(expression):
    stack = Stack()

    for exp in expression:
        if exp.isdigit():
            stack.push(int(exp))
        else:
            op2 = stack.pop()
            op1 = stack.pop()

            if exp == '+':
                stack.push(op1 + op2)
            elif exp == '-':
                stack.push(op1 - op2)
            elif exp == '*':
                stack.push(op1 * op2)
            else:
                stack.push(op1 / op2)
    
    return stack.peek()

if __name__ == '__main__':
    
    # 테스트
    expression = "{[()]}"
    print(f"{expression} is balanced: {is_valid(expression)}")

    expression = "{[(])}"
    print(f"{expression} is balanced: {is_valid(expression)}")

    # 테스트 2
    expression = '347*+'
    print(f"후위 표기식: {is_valid_postfix(expression)}")

    expression = '34+7/'
    print(f"후위 표기식: {is_valid_postfix(expression)}")