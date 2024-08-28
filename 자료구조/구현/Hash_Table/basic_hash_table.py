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
    
