class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def hash_function(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = Node(key, value, self.table[index])
    def find(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False

# Testimine
ht = HashTable(10)
ht.insert("Mart", "Professor")
ht.insert("Test", "123")
ht.insert("Mart", "Updated")
print(ht.find("Mart"))  
print(ht.find("Test"))  
print(ht.find("Missing")) 
ht.delete("Test")
print(ht.find("Test"))  

#Ajakompleksus Separate Chaining O(1) 
#Ruumikompleksus Separate Chaining O(n)
#Ajakompleksus Open Addressing O(n)
#Ruumikompleksus Open Addressing O(1)

#Plussid: Kerge kasutada, räsitabel ei saa kunagi täis ja on vähem tundlik räsifunktsioonile või koormustegurile
#Miinused: Kasutab rohkem mälu. Halvimal juhul tegu lineaarotsinguga. 