import random

class RandomizedSet:
    def __init__(self):
        self.values = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val not in self.index:
            index = len(self.values)
            self.values.append(val)
            self.index[val] = index
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.index:
            last_element = self.values[-1]
            remove_index = self.index[val]

            self.values[remove_index] = last_element
            
            self.values.pop()
            self.index[last_element] = remove_index
            del self.index[val]
            """
            Take the last element and replace it with current element
            """
            return True
        else:
            return False
    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()