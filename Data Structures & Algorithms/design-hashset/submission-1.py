class MyHashSet:

    def __init__(self):
        self.myhashset = []

    def add(self, key: int) -> None:
        if key not in self.myhashset:
            self.myhashset.append(key)

    def remove(self, key: int) -> None:
        if key in self.myhashset:
            self.myhashset.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.myhashset:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)