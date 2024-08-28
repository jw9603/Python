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



