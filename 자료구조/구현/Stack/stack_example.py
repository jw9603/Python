from stack import Stack
def is_balanced(expression):
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

# 테스트
expression = "{[()]}"
print(f"{expression} is balanced: {is_balanced(expression)}")

expression = "{[(])}"
print(f"{expression} is balanced: {is_balanced(expression)}")