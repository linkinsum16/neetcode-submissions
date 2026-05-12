class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        for i, item in enumerate(self.hashmap):
            if key == item[0]:
                item[1] = value
                return
        
        self.hashmap.append([key,value])

    def get(self, key: int) -> int:
        for item in self.hashmap:
            if key == item[0]:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        for item in self.hashmap:
            if key == item[0]:
              self.hashmap.remove(item)  


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)