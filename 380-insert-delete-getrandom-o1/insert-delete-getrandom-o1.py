import random
class RandomizedSet:

    def __init__(self):
        self.index = {}
        self.randomSet = []

    def insert(self, val: int) -> bool:
        if val in self.index and self.index[val] != -1:
            return False
        else:
            self.randomSet.append(val)
            self.index[val] = len(self.randomSet) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.index or self.index[val] == -1:
            return False
        removeIndex = self.index[val]

        self.index[self.randomSet[-1]] = removeIndex
        self.index[val] = -1

        self.randomSet[removeIndex], self.randomSet[-1] = self.randomSet[-1], self.randomSet[removeIndex]

        self.randomSet.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.randomSet)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()