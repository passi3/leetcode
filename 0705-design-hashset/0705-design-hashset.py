class MyHashSet:

    def __init__(self):
        self.size = 1009
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        idx = self._hash(key)

        if key not in self.table[idx]:
            self.table[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        
        if key in self.table[idx]:
            self.table[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)

        return key in self.table[idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)