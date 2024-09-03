## [파이썬 자료구조] 해시 테이블

오늘 소개할 자료 구조는 해시 테이블입니다.

그럼 살펴보겠습니다.

### 해시란 무엇인가?

해시는 **데이터(일반적으로 문자열이나 숫자)를 고정된 크기의 값으로 변환하는 과정**입니다. 이 변환 과정에서 사용되는 함수가 바로 **해시 함수(Hash Function)**입니다. 해시 함수는 임의의 길이를 가진 입력 데이터를 받아들이고, 이를 고정된 길이의 해시 값(해시 코드 또는 해시 인덱스)으로 변환합니다.

예를 들어, "apple"이라는 문자열을 해시 함수에 입력하면 이 문자열을 특정 숫자(예: 4)로 변환하는 것입니다. 이 숫자는 해시 테이블이라는 자료 구조에서 해당 데이터가 저장될 위치를 나타냅니다.

## 1. 해시 구조

해시 테이블은 **키(Key)**와 **값(Value)** 쌍을 저장하는 데이터 구조로, 매우 효율적으로 데이터를 저장하고 검색할 수 있게 해줍니다. 해시 테이블은 내부적으로 배열(array)로 구현되며, 해시 함수에 의해 생성된 해시 값을 사용해 배열의 인덱스를 결정합니다.

- **키(Key)**: 데이터를 식별하는 데 사용되는 값입니다. 예를 들어, "사과"라는 단어를 저장하려고 할 때, "사과"가 키가 될 수 있습니다.
- **값(Value)**: 키에 연관된 실제 데이터입니다. 예를 들어, "사과"의 키에 연관된 가격 정보가 값이 될 수 있습니다.
- 해시 테이블(Hash Table): 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
- 해시 함수(Hash Function): 키에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
- 해시 값(Hash value) 또는 해시 주소(Hash Address): 키를 해시 함수로 연산해서, 해시 값을 알아내고, 이를 기반으로 해시 테이블에서 해당 키에 대한 데이터 위치를 일관성 있게 찾을 수 있음
- 슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간
- 저장할 데이터에 대해 Key를 추출할 수 있는 별도 함수도 존재할 수 있음

![](https://velog.velcdn.com/images/jw9603/post/61706ccb-be63-4c54-bdbe-9243d86befae/image.png)


해시 테이블은 다음과 같은 절차로 작동합니다:

1. **입력된 키**에 대해 해시 함수를 사용하여 해시 값을 계산합니다.
2. 이 해시 값(해시 주소)에 따라 해시 테이블의 특정 위치에 값을 저장합니다.
3. 데이터를 검색할 때도 동일한 해시 함수를 사용하여 키의 해시 값을 계산하고, 해당 위치에서 값을 빠르게 찾을 수 있습니다.

---

## 2. 해시의 장점과 단점

**장점:**

- **빠른 검색 속도**: 해시 테이블은 평균적으로 O(1)의 시간 복잡도로 데이터를 검색할 수 있습니다. 이는 큰 데이터셋에서도 매우 빠른 검색을 가능하게 합니다.
- **효율적인 메모리 사용**: 해시 테이블은 데이터를 저장할 때 필요한 메모리 공간을 효과적으로 사용합니다.

**단점:**

- **충돌(Collision)**: 서로 다른 두 키가 동일한 해시 값을 갖게 되는 경우 충돌이 발생할 수 있습니다. 이는 해시 테이블의 성능을 저하시킬 수 있습니다. 이 문제를 해결하기 위해 충돌 처리 방법이 필요합니다.
- **해시 함수의 중요성**: 잘못된 해시 함수는 많은 충돌을 일으켜 해시 테이블의 효율성을 크게 떨어뜨릴 수 있습니다.

이제 해시의 개념과 해시 테이블의 작동 방식을 이해했으니, 다음 단계에서는 파이썬으로 해시 테이블을 직접 구현해보고, 충돌을 처리하는 다양한 방법에 대해 알아보겠습니다.

---

## 3. 파이썬으로 해시 테이블 구현

우선, 충돌을 제외한 기본적인 해시 테이블 구현을 위한 파이썬 코드를 제공하겠습니다. 이 코드는 단순히 해시 함수를 사용하여 키를 배열의 인덱스로 변환하고, 해당 위치에 값을 저장하거나 검색하는 방식으로 작동합니다.

### 파이썬으로 기본 해시 테이블 구현

```python
class BasicHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        """간단한 해시 함수 구현"""
        return hash(key) % self.size

    def insert(self, key, value):
        """키-값 쌍을 해시 테이블에 삽입"""
        index = self._hash(key)
        self.table[index] = value

    def search(self, key):
        """키로 값을 검색"""
        index = self._hash(key)
        return self.table[index]

    def delete(self, key):
        """키-값 쌍을 삭제"""
        index = self._hash(key)
        self.table[index] = None

    def __str__(self):
        """해시 테이블의 내용을 보기 좋게 출력"""
        return str(self.table)

```

### 사용 예제

이제 위에서 구현한 해시 테이블을 사용하여 키-값 쌍을 삽입, 검색, 삭제하는 예제를 보겠습니다.

```python
ht = BasicHashTable()

ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("orange", 300)

print("Search apple:", ht.search("apple"))  # Output: 100
print("Search banana:", ht.search("banana"))  # Output: 200

ht.delete("orange")
print("Deleted orange:", ht.search("orange"))  # Output: None

print(ht)

```

이 구현에서는 충돌 처리를 고려하지 않았습니다. 따라서 동일한 해시 값을 가진 두 개의 키가 발생할 경우, 마지막으로 삽입된 값이 기존 값을 덮어쓰게 됩니다. 이 간단한 구현은 해시 테이블의 기본 개념을 이해하는 데 유용합니다.

다음 단계에서는 충돌을 처리하는 방법에 대해 다루거나, 해시 함수를 최적화하는 방법에 대해 살펴볼 수 있습니다.

전체 코드는 아래와 같습니다:

```python
class BasicHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        """간단한 해시 함수 구현"""
        return hash(key) % self.size

    def insert(self, key, value):
        """키-값 쌍을 해시 테이블에 삽입"""
        index = self._hash(key)
        self.table[index] = value

    def search(self, key):
        """키로 값을 검색"""
        index = self._hash(key)
        return self.table[index]

    def delete(self, key):
        """키-값 쌍을 삭제"""
        index = self._hash(key)
        self.table[index] = None

    def __str__(self):
        """해시 테이블의 내용을 보기 좋게 출력"""
        return str(self.table)
    
    
if __name__ == '__main__':
    ht = BasicHashTable()

    ht.insert("apple", 100)
    ht.insert("banana", 200)
    ht.insert("orange", 300)

    print("Search apple:", ht.search("apple"))  # Output: 100
    print("Search banana:", ht.search("banana"))  # Output: 200

    ht.delete("orange")
    print("Deleted orange:", ht.search("orange"))  # Output: None

    print(ht)
```

---

## 4. 해시 테이블에서의 충돌 (Collision)

해시 테이블에서 충돌이란 **서로 다른 두 개 이상의 키가 동일한 해시 값**을 갖게 되는 경우를 말합니다.

예를 들어, `hash("apple")`과 `hash("orange")`가 동일한 인덱스를 반환하면, 두 값이 동일한 슬롯에 저장되어야 합니다. 그러나 해시 테이블은 각 슬롯에 하나의 값만 저장할 수 있으므로 충돌을 처리하는 방법이 필요합니다.

### 4.1 충돌의 원인

충돌이 발생하는 주요 원인은 해시 함수가 반환하는 해시 값의 범위가 제한적이기 때문입니다. 해시 테이블의 크기가 제한되어 있기 때문에, 여러 개의 서로 다른 키가 같은 해시 값으로 매핑될 가능성이 존재합니다. 이러한 충돌을 처리하지 않으면 데이터의 저장 및 검색이 올바르게 이루어지지 않습니다.

### 4.2 충돌 처리 방법

충돌을 처리하는 방법에는 여러 가지가 있으며, 가장 일반적으로 사용되는 방법은 다음과 같습니다.

**1. 체이닝 (Chaining)**

체이닝은 각 슬롯이 연결 리스트를 갖도록 하여, 충돌이 발생한 경우 해당 슬롯에 값을 연결 리스트의 형태로 저장하는 방법입니다. 이 방식은 충돌이 발생해도 추가적인 값을 같은 슬롯에 연결하여 저장할 수 있습니다.

![](https://velog.velcdn.com/images/jw9603/post/b7d68eed-5df6-43c7-bd7e-2b3b0d8f79f6/image.png)


**2. 개방 주소법 (Open Addressing)**

개방 주소법은 충돌이 발생했을 때 **다른 슬롯**을 찾아 값을 저장하는 방법입니다. 이 방법에는 다음과 같은 세 가지 기법이 포함됩니다:

- **선형 탐사 (Linear Probing)**: 충돌이 발생하면 다음 슬롯(현재 인덱스 + 1)을 탐색하여 빈 슬롯을 찾습니다.
- **이차 탐사 (Quadratic Probing)**: 탐사 과정에서 제곱수를 더하여 다음 위치를 결정합니다. 예를 들어, 충돌이 발생하면 1^2, 2^2, 3^2... 위치를 차례로 탐색합니다.
- **이중 해싱 (Double Hashing)**: 두 번째 해시 함수를 사용하여 새로운 해시 값을 계산한 후, 해당 위치로 이동합니다.

### 4.3 체이닝을 통한 충돌 처리 구현

이제, 체이닝을 이용하여 충돌을 처리하는 해시 테이블을 구현해보겠습니다.

```python
class ChainedHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # 각 슬롯에 빈 리스트를 초기화
    
    def hash_function(self, key):
        """간단한 해시 함수 구현"""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """키-값 쌍을 해시 테이블에 삽입"""
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # 키-값 쌍을 체이닝 리스트에 추가
        self.table[index].append([key, value])
    
    def search(self, key):
        """키로 값을 검색"""
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def delete(self, key):
        """키-값 쌍을 삭제"""
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def __str__(self):
        """해시 테이블의 내용을 보기 좋게 출력"""
        return "\n".join([f"Index {i}: {ll}" for i, ll in enumerate(self.table)])

    
if __name__ == '__main__':
    ht = ChainedHashTable()

    ht.insert("apple", 100)
    ht.insert("banana", 200)
    ht.insert("orange", 300)
    ht.insert("grape", 400)
    ht.insert("watermelon", 100)

    print("Search apple:", ht.search("apple"))  # Output: 100
    print("Search banana:", ht.search("banana"))  # Output: 200

    ht.insert("banana", 250)
    print("Updated banana:", ht.search("banana"))  # Output: 250

    ht.delete("orange")
    print("Deleted orange:", ht.search("orange"))  # Output: None

    print(ht)
    '''
    Index 0: []
    Index 1: []
    Index 2: []
    Index 3: [['banana', 250], ['watermelon', 100]]
    Index 4: []
    Index 5: []
    Index 6: []
    Index 7: []
    Index 8: []
    Index 9: [['apple', 100], ['grape', 400]]
    '''

```

### 코드 설명:

1. **해시 테이블 구조**:
    - `self.table`은 각 슬롯이 리스트로 초기화된 크기 `size`의 리스트입니다. 이 리스트는 체이닝 기법을 통해 동일한 해시 인덱스에서 발생하는 충돌을 처리합니다.
2. **삽입 (`insert`)**:
    - 키에 대한 해시 인덱스를 계산한 후, 해당 슬롯(리스트)에 이미 같은 키가 존재하는지 확인합니다. 존재하면 값을 업데이트하고, 없으면 리스트에 새 키-값 쌍을 추가합니다.
3. **검색 (`search`)**:
    - 키에 대한 해시 인덱스를 계산한 후, 해당 인덱스에 있는 리스트를 순회하면서 키를 찾아 값을 반환합니다.
4. **삭제 (`delete`)**:
    - 키에 대한 해시 인덱스를 계산한 후, 해당 인덱스에 있는 리스트를 순회하면서 키를 찾아 삭제합니다.
5. **출력 (`__str__`)**:
    - 해시 테이블의 각 슬롯에 저장된 키-값 쌍들을 보기 좋게 출력합니다.

이 코드에서는 각 슬롯이 리스트로 구현되어 있어, 동일한 해시 인덱스를 가진 키-값 쌍들이 리스트의 각 요소로 저장됩니다. 연결 리스트를 사용한 구현과 비교했을 때, 리스트를 사용하는 이 방식은 파이썬의 기본 자료구조를 활용하여 더 간단하게 체이닝 기법을 구현할 수 있습니다.

---

## 5. 파이썬에서 해시는?

파이썬에서 해시 테이블은 대부분의 프로그래밍 언어에서처럼 중요한 자료 구조입니다. 파이썬에서는 해시 테이블을 직접 구현할 필요 없이, **딕셔너리(`dict`)**라는 내장 자료 구조를 통해 쉽게 사용할 수 있습니다.

### 딕셔너리(`dict`)란 무엇인가?

딕셔너리는 **키-값 쌍**을 저장하는 자료 구조로, 키를 사용하여 값을 빠르게 검색할 수 있도록 설계되어 있습니다. 딕셔너리의 작동 원리는 해시 테이블과 동일하며, 파이썬에서는 매우 효율적인 해시 테이블이 구현되어 있습니다.

```python
# 딕셔너리 생성 예시
fruit_prices = {
    "apple": 100,
    "banana": 200,
    "orange": 300
}

# 값 검색
print(fruit_prices["apple"])  # Output: 100

# 값 삽입
fruit_prices["grape"] = 400

# 값 삭제
del fruit_prices["orange"]

# 값 변경
fruit_prices['apple'] = 1000

print(fruit_prices)  # Output: {'apple': 100, 'banana': 200, 'grape': 400}
```

### 파이썬 딕셔너리의 특징

- **빠른 검색 속도**: 파이썬 딕셔너리는 해시 테이블을 기반으로 구현되어 있어, 평균적으로 O(1)의 시간 복잡도로 데이터를 검색할 수 있습니다.
- **자동 충돌 처리**: 딕셔너리는 내부적으로 충돌을 처리하는 메커니즘을 가지고 있습니다. 파이썬 개발자가 충돌 처리에 대해 걱정할 필요 없이, 딕셔너리를 사용할 수 있습니다.
- **임의 순서 유지**: 파이썬 3.7 이후부터 딕셔너리는 삽입 순서를 유지합니다. 이는 해시 테이블과 순차적 데이터 구조의 장점을 결합한 것입니다.

### 딕셔너리의 해시 함수

파이썬에서 딕셔너리의 키는 해시 가능한 객체여야 합니다. 즉, 키는 변경 불가능한(immutable) 데이터 타입이어야 하며, 이를 통해 고유한 해시 값을 계산할 수 있습니다. 문자열, 숫자, 튜플 등이 대표적인 해시 가능한 타입입니다.

```python
# 해시 가능한 키 예시
print(hash("apple"))  # 문자열의 해시 값
print(hash(42))  # 정수의 해시 값
print(hash((1, 2, 3)))  # 튜플의 해시 값

```

### 딕셔너리의 내부 동작 방식

파이썬 딕셔너리는 해시 함수를 사용하여 키의 해시 값을 계산한 후, 해당 값을 기반으로 내부 배열에서 데이터를 저장하고 검색합니다. 충돌이 발생할 경우, 파이썬은 체이닝이나 개방 주소법과 같은 기법을 사용하여 충돌을 처리합니다.

이처럼 파이썬의 딕셔너리는 사용자가 직접 해시 테이블을 구현하지 않아도, 강력하고 효율적인 해시 구조를 손쉽게 사용할 수 있게 해줍니다. 이는 파이썬의 생산성을 크게 높여주는 중요한 요소 중 하나입니다.

### 결론

파이썬의 딕셔너리는 해시 테이블의 강력한 기능을 제공하면서도, 매우 사용하기 쉽도록 설계되어 있습니다. 해시 테이블을 이해하고 직접 구현해보는 것은 중요한 학습 경험이지만, 실제 파이썬 코드에서는 딕셔너리를 사용하여 대부분의 해시 관련 작업을 수행할 수 있습니다. 이는 파이썬이 강력한 이유 중 하나이며, 개발자에게 큰 이점을 제공합니다.

---

## 마무리

오늘은 해시 테이블 자료 구조에 대해 알아보았는데요. 개념은 간단하지만, 구현하는데 있어서 좀 까다로운 편이였습니다. 하지만, 파이썬을 사용한다면? 딕셔너리라는 어마무시한 자료형이 있기 때문에, 사용하기 쉽다는점!

결론은 뭐다? 파이썬을 사용하자!

다음 포스팅은 매우 어려울 것으로 예상되는 트리입니다. 

긴 글 읽어주셔서 감사합니다!

![](https://velog.velcdn.com/images/jw9603/post/27cfecc0-af21-4b9d-8bf0-a9c01bcb0c4d/image.png)


더 나은 개발자가 될거야! ⭐

➕ 리스트가 아닌 링크드 리스트를 통해서도 해시 테이블과 체이닝 기법을 구현할 수 있습니다. 아래 코드를 참조하시면 좋을것 같습니다.
- Linked_List.py
- chaining_linked_list.py

## References

- https://hik-coding.tistory.com/298
- https://en.wikipedia.org/wiki/Hash_table
