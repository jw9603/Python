# [파이썬 자료구조] 스택

### 자료구조 스택 (Stack) 이해하기

스택(Stack)은 데이터 구조 중 하나로, 데이터가 나중에 들어온 것이 먼저 나가는 **LIFO**(Last In, First Out) 방식으로 동작합니다. 스택을 사용하면 웹 브라우저의 뒤로 가기 기능, 텍스트 편집기의 실행 취소(undo) 기능 등 다양한 곳에서 유용하게 활용할 수 있습니다.

이번 포스팅에서는 스택의 기본 개념을 설명하고, Python을 사용하여 스택을 구현하는 방법을 단계별로 소개하겠습니다.

---

### 1. 스택의 기본 개념

스택은 기본적으로 두 가지 주요 연산을 지원합니다:

- **push**: 스택의 가장 위에 새로운 요소를 추가합니다.
- **pop**: 스택의 가장 위에 있는 요소를 제거하고 반환합니다.

추가적으로, 다음과 같은 연산이 있을 수 있습니다:

- **peek**: 스택의 가장 위에 있는 요소를 반환하지만 제거하지는 않습니다.
- **is_empty**: 스택이 비어 있는지 확인합니다.
- **size**: 스택에 있는 요소의 개수를 반환합니다.

스택의 대표적인 예로는 책을 쌓아 올리는 것을 생각할 수 있습니다. 책을 한 권씩 쌓아 올리면 나중에 쌓은 책을 먼저 꺼낼 수 있습니다.

아래 링크를 통해 직접 스택 자료구조를 이해할 수 있습니다.

[Linked List (Single, Doubly), Stack, Queue, Deque - VisuAlgo](https://visualgo.net/en/list)

![image](https://github.com/user-attachments/assets/9f8b7fec-5009-4e17-bc03-e685fa74f4d0)


---

### 2. Python으로 스택 구현하기

이제 Python을 사용하여 스택을 직접 구현해보겠습니다. Python에서는 리스트(List)를 사용하여 스택을 간단하게 구현할 수 있습니다.

```python
class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('You popped from an empty stack')

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("You peeked from an empty stack")

    def size(self):
        return len(self.items)

    def __repr__(self):
        return f"Stack({self.items})"

    def __str__(self):
        return str(self.items)

```

위 코드는 `Stack` 클래스의 기본 구조를 보여줍니다. 각 메서드를 하나씩 살펴보겠습니다.

- `__init__`: 스택을 초기화합니다. 내부적으로는 리스트 `self.items`를 사용하여 스택을 구현합니다.
- `is_empty`: 스택이 비어 있는지 여부를 확인합니다. `self.items`의 길이가 0이면 비어 있는 것으로 간주합니다.
- `push`: 스택의 맨 위에 새로운 요소를 추가합니다. Python 리스트의 `append()` 메서드를 사용하여 요소를 추가합니다.
- `pop`: 스택의 맨 위에 있는 요소를 제거하고 반환합니다. 리스트의 `pop()` 메서드를 사용합니다.
- `peek`: 스택의 맨 위에 있는 요소를 반환하지만, 제거하지는 않습니다. 리스트의 마지막 요소를 반환합니다.
- `size`: 스택에 있는 요소의 개수를 반환합니다.
- `__repr__`: 스택 객체의 문자열 표현을 반환합니다. 이 메서드는 주로 디버깅을 위해 사용되며, `Stack` 객체의 더 자세한 정보를 포함할 수 있도록 디자인되었습니다.
- `__str__`: 스택의 현재 상태를 문자열로 반환합니다. 주로 사용자가 객체를 더 쉽게 이해할 수 있도록 가독성을 고려한 출력 포맷을 제공합니다.

### `__repr__`와 `__str__`의 차이점

Python에서는 객체를 문자열로 표현할 때 `__repr__`와 `__str__`라는 두 가지 메서드를 사용할 수 있습니다. 이 두 메서드는 비슷해 보이지만, 그 목적과 사용 용도가 다릅니다.

- **`__repr__`**: 객체의 공식적인 문자열 표현을 반환합니다. 주로 개발자가 객체의 상태를 확인하거나, 디버깅할 때 유용하게 사용됩니다. 일반적으로 `__repr__`은 객체를 가능한 한 Python 코드에서 사용할 수 있는 형태로 반환해야 합니다. 예를 들어, `Stack([1, 2, 3])`처럼 객체를 재생성할 수 있는 문자열을 반환하는 것이 이상적입니다. `__repr__`은 `repr()` 함수나, 객체를 콘솔에서 입력했을 때 호출됩니다.
- **`__str__`**: 객체의 비공식적인(사용자 친화적인) 문자열 표현을 반환합니다. 사용자가 객체를 쉽게 이해할 수 있도록 하는 데 중점을 둡니다. 주로 `print()` 함수나 `str()` 함수에서 호출됩니다. `__str__`은 사용자가 객체의 상태를 확인할 때 읽기 쉬운 형식으로 정보를 제공하는 데 사용됩니다.

### `__repr__`와 `__str__`의 예

```python
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(str(stack))  # __str__ 호출, 출력 결과: [1, 2, 3]
print(repr(stack))  # __repr__ 호출, 출력 결과: Stack([1, 2, 3])

```

- `str(stack)`은 `__str__` 메서드를 호출하여 스택의 요소만 보여주는 간단한 문자열 `[1, 2, 3]`을 반환합니다.
- `repr(stack)`은 `__repr__` 메서드를 호출하여 스택의 클래스명과 내부 상태를 보여주는 `Stack([1, 2, 3])`을 반환합니다.

이처럼 `__str__`은 사용자가 객체를 쉽게 이해할 수 있도록 하는 데 주로 사용되고, `__repr__`은 객체의 정확한 상태를 개발자가 확인할 수 있도록 합니다. 만약 `__str__` 메서드가 정의되지 않은 경우, `print()` 함수 등에서 `__repr__`이 대신 호출됩니다.

---

### 3. 스택 사용 예시

이제 위에서 구현한 스택을 실제로 사용해 보겠습니다.

```python
# 스택 생성
stack = Stack()

# 스택에 요소 추가
stack.push(1)
stack.push(2)
stack.push(3)
print(f"스택 상태: {stack}")

# 스택에서 요소 제거
print(f"pop: {stack.pop()}")
print(f"스택 상태: {stack}")

# 스택의 맨 위 요소 확인
print(f"peek: {stack.peek()}")
print(f"스택 상태: {stack}")

# 스택의 크기 확인
print(f"스택 크기: {stack.size()}")

# 스택 비어 있는지 확인
print(f"스택이 비어 있는가? {stack.is_empty()}")

```

출력 결과:

```
스택 상태: [1, 2, 3]
pop: 3
스택 상태: [1, 2]
peek: 2
스택 상태: [1, 2]
스택 크기: 2
스택이 비어 있는가? False

```

위 예시를 통해 스택의 동작 방식을 쉽게 이해할 수 있습니다.

---

### 4. Python의 `deque` 라이브러리로 스택 구현하기

Python의 `collections` 모듈에서 제공하는 `deque`(double-ended queue)를 사용하여 스택을 효율적으로 구현할 수도 있습니다. `deque`는 양쪽에서 요소를 추가하거나 제거할 수 있는 자료구조로, 스택의 `LIFO` 동작을 매우 빠르게 수행할 수 있습니다. 리스트를 사용한 스택 구현과 달리, `deque`는 양 끝에서의 삽입과 삭제가 O(1) 시간 복잡도로 이루어집니다.

아래는 `deque`를 사용한 스택 구현 예제입니다.

```python
from collections import deque

class Stack:

    def __init__(self):
        self.items = deque() # [] 대신 deque(), deque([])처럼 해도 됨

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('You popped from an empty stack')

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("You peeked from an empty stack")

    def size(self):
        return len(self.items)

    def __repr__(self):
        return f"Stack({list(self.items)})"

    def __str__(self):
        return str(list(self.items))

```

`deque`를 사용하여 구현된 스택은 리스트를 사용한 것과 동일한 기능을 가지며, 더 나은 성능을 제공합니다. 특히 스택이 커질수록 `deque`를 사용한 구현이 더 효율적입니다.

---

### 5. 스택 (deque) 사용 예시

이제 위에서 구현한 스택을 실제로 사용해 보겠습니다.

```python
# 스택 생성
stack = Stack()

# 스택에 요소 추가
stack.push(1)
stack.push(2)
stack.push(3)
print(f"스택 상태: {stack}")

# 스택에서 요소 제거
print(f"pop: {stack.pop()}")
print(f"스택 상태: {stack}")

# 스택의 맨 위 요소 확인
print(f"peek: {stack.peek()}")
print(f"스택 상태: {stack}")

# 스택의 크기 확인
print(f"스택 크기: {stack.size()}")

# 스택 비어 있는지 확인
print(f"스택이 비어 있는가? {stack.is_empty()}")

```

출력 결과:

```less
less코드 복사
스택 상태: [1, 2, 3]
pop: 3
스택 상태: [1, 2]
peek: 2
스택 상태: [1, 2]
스택 크기: 2
스택이 비어 있는가? False

```

위 예시를 통해 스택의 동작 방식을 쉽게 이해할 수 있습니다.

---

### 5. 스택의 실제 활용 예

스택은 알고리즘 문제 해결 시 자주 사용됩니다. 예를 들어, 괄호의 유효성을 검사하는 문제에서는 스택을 사용하여 여는 괄호와 닫는 괄호를 짝짓는 작업을 수행할 수 있습니다.

다음은 괄호 유효성 검사를 위한 코드 예시입니다.

```python
def is_balanced(expression):
    stack = Stack()
    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            top = stack.pop()
            if (top == '(' and char != ')') or \\
               (top == '[' and char != ']') or \\
               (top == '{' and char != '}'):
                return False
    return stack.is_empty()

# 테스트
expression = "{[()]}"
print(f"{expression} is balanced: {is_balanced(expression)}")

expression = "{[(])}"
print(f"{expression} is balanced: {is_balanced(expression)}")

```

출력 결과:

```
{[()]} is balanced: True
{[(])} is balanced: False

```

이 코드는 스택을 사용하여 괄호가 제대로 짝지어져 있는지 확인합니다. 여는 괄호는 스택에 쌓고, 닫는 괄호를 만나면 스택에서 꺼내어 짝이 맞는지 확인합니다.

---

### 6. 스택 자료구조의 시간 복잡도
스택의 기본 연산인 push, pop, peek, is_empty 등의 연산은 모두 O(1)의 시간 복잡도를 가집니다. 이는 이러한 연산이 스택의 크기에 상관없이 일정한 시간 안에 수행될 수 있음을 의미합니다.

- push(item): 스택의 맨 위에 요소를 추가하는 연산으로, 시간 복잡도는 O(1)입니다.
- pop(): 스택의 맨 위 요소를 제거하고 반환하는 연산으로, 시간 복잡도는 O(1)입니다.
- peek(): 스택의 맨 위 요소를 확인하는 연산으로, 시간 복잡도는 O(1)입니다.
- is_empty(): 스택이 비어 있는지 확인하는 연산으로, 시간 복잡도는 O(1)입니다.
- size(): 스택에 있는 요소의 개수를 반환하는 연산으로, 시간 복잡도는 O(1)입니다.
- search(item): 스택에서 특정 요소를 찾는 연산의 시간 복잡도는 O(n)입니다.

스택의 각 연산은 대부분 O(1) 시간 복잡도를 가지므로, 스택은 매우 빠르고 효율적인 자료구조입니다. 하지만 검색 연산은 스택의 모든 요소를 확인해야 하므로, 검색이 자주 필요하다면 다른 자료구조를 고려하는 것이 좋습니다.

---

### 7. 스택 구조와 프로세스 스택

재귀 함수 호출 과정은 실제로 **스택(Stack)**과 동일한 방식으로 동작합니다. 이를 이해하기 위해 재귀 함수가 호출되는 과정을 살펴보겠습니다.

### 재귀 함수와 스택의 관계

재귀 함수는 함수가 자기 자신을 호출하는 방식입니다. 이때, 각 함수 호출은 독립적인 실행 컨텍스트(지역 변수, 매개 변수, 리턴 주소 등)를 갖습니다. 함수가 호출될 때마다 이 실행 컨텍스트가 **호출 스택(Call Stack)**에 쌓이게 됩니다.

스택은 **LIFO**(Last In, First Out) 방식으로 동작하기 때문에, 가장 나중에 호출된 함수가 가장 먼저 종료되고, 호출 스택에서 제거됩니다. 이것이 재귀 함수의 실행 과정과 동일합니다.

### 재귀 호출 과정의 예

다음은 간단한 재귀 함수의 예입니다:

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

```

이 `factorial` 함수는 입력된 값 `n`의 팩토리얼을 계산합니다. 예를 들어, `factorial(3)`을 호출하면 다음과 같은 과정이 발생합니다.

1. `factorial(3)`이 호출되면, `n`이 1이 아니므로 `factorial(2)`를 호출합니다.
2. `factorial(2)`이 호출되면, 다시 `factorial(1)`을 호출합니다.
3. `factorial(1)`은 기본 조건을 만족하므로 1을 반환합니다.
4. 이제 `factorial(2)`는 `2 * factorial(1)`을 계산하고, 2를 반환합니다.
5. 마지막으로 `factorial(3)`은 `3 * factorial(2)`를 계산하고, 6을 반환합니다.

이 과정에서 각 호출이 스택에 쌓이고, 마지막 호출(`factorial(1)`)부터 시작하여 차례로 계산된 결과가 반환되면서 스택에서 제거됩니다.

### 호출 스택의 동작

- `factorial(3)` 호출: 호출 스택에 `factorial(3)`이 쌓입니다.
- `factorial(2)` 호출: 호출 스택에 `factorial(2)`가 추가됩니다.
- `factorial(1)` 호출: 호출 스택에 `factorial(1)`이 추가됩니다.

이제 스택의 맨 위에 있는 `factorial(1)`이 종료되면 스택에서 제거되고, 그 결과는 `factorial(2)`로 전달됩니다. 이 과정이 반복되면서 호출된 함수들이 순차적으로 스택에서 제거됩니다.

### 예시

```python
# 재귀 함수
def recursive(data):
    if data < 0:
        print ("ended")
    else:
        print(data)
        recursive(data - 1)
        print("returned", data) 
        
print(recursive(4))
# 4
# 3
# 2
# 1
# 0
# ended
# returned 0
# returned 1
# returned 2
# returned 3
# returned 4
```

재귀 함수 호출 과정은 호출 스택(Call Stack)을 사용하며, 이는 스택 자료구조의 동작 방식과 동일합니다. 각 함수 호출은 스택의 한 레벨에 쌓이고, 마지막 호출부터 차례로 스택에서 제거되면서 함수가 종료됩니다. 따라서 재귀 함수는 본질적으로 스택을 사용하는 함수 호출 구조와 밀접하게 연결되어 있습니다.

---

### 결론

스택은 매우 기본적이면서도 강력한 자료구조입니다. Python을 활용하면 스택을 쉽게 구현하고 다양한 문제 해결에 적용할 수 있습니다. 이 블로그에서는 스택의 기본 개념과 구현 방법을 설명했고, Python을 사용한 예제 코드를 통해 스택의 동작 원리를 살펴보았습니다. 스택을 이해하고 활용할 수 있다면, 더 복잡한 자료구조나 알고리즘을 이해하는 데 큰 도움이 될 것입니다.

https://velog.io/@jw9603/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9D

읽어주셔서 감사합니다!
