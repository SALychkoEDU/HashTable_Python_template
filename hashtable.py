class HashTable:
    def __init__(self, size: int):
        self.array = [[] for i in range(size)] # каждый элемент массива ссылается на список
        self.size = size                # размер массива
    def getIndex(self, key):
        """Получает индекс по ключу"""
        return abs(hash(key) % self.size)
    def __getitem__(self, key):
        self.get(key)
    def __setitem__(self, key, value):
        self.set(key)
    def __delitem__(self, key):
        self.delete(self, key)
    def __contains__(self, key):
        return self.contains(key)
    def __iter__(self):
        """Возвращает итератор по всем элементам таблицы"""
        return None
    def __repr__(self):
        return f'HashTable{str(tuple(self))}'

class HashMap(HashTable):
    def __init__(self, size):
        super().__init__(size)

    def get(self, key):
        return None

    def set(self, key, value):
        pass

    def delete(self, key):
        pass

    def contains(self, key):
        return False

class HashSet(HashTable):
    def __init__(self, size):
        super().__init__(size)

    def get(self, key):
        return None

    def set(self, key):
        pass

    def delete(self, key):
        pass

    def contains(self, key):
        return False

    def intersection(self, setB: "HashSet") -> "HashSet":
        return None

    def difference(self, setB: "HashSet") -> "HashSet":
        return None

    def union(self, setB: "HashSet") -> "HashSet":
        return None