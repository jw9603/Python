from Linked_List import LinkedList
class HashTable_LL:
    
    def __init__(self,size=10):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]
        
        
    def hash_function(self,key):
        
        return hash(key) % self.size
    
    def insert(self,key,value):
        
        index = self.hash_function(key)
        
        self.table[index].insert(key,value)
        
    def search(self,key):
        index = self.hash_function(key)
        return self.table[index].search(key)   

    def delete(self,key):
        index = self.hash_function(key)
        self.table[index].delete(key)
        
    def __str__(self):
        result = []
        
        for i, ll in enumerate(self.table):
            result.append(f"Index {i}: {ll}")
        return '\n'.join(result)
    
if __name__ == '__main__':
    
    ht = HashTable_LL()
    
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
    