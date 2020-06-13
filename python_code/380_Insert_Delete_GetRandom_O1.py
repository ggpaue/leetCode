#Design a data structure that supports all following operations in average O(1) time.

#insert(val): Inserts an item val to the set if not already present.
#remove(val): Removes an item val from the set if present.
#getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
#Example:

#// Init an empty set.
#RandomizedSet randomSet = new RandomizedSet();

#// Inserts 1 to the set. Returns true as 1 was inserted successfully.
#randomSet.insert(1);

#// Returns false as 2 does not exist in the set.
#randomSet.remove(2);

#// Inserts 2 to the set, returns true. Set now contains [1,2].
#randomSet.insert(2);

#// getRandom should return either 1 or 2 randomly.
#randomSet.getRandom();

#// Removes 1 from the set, returns true. Set now contains [2].
#randomSet.remove(1);

#// 2 was already in the set, so return false.
#randomSet.insert(2);

#// Since 2 is the only number in the set, getRandom always return 2.
#randomSet.getRandom();

import random
import math
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.direct = {}
        self.revert = {}
        self.count = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.revert:
            return False
        else:
            self.revert[val] = self.count
            self.direct[self.count] = val
            self.count += 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.revert:
            return False
        else:
            index = self.revert.pop(val)
            self.direct.pop(index)
            if index != self.count-1:
                self.direct[index] = self.direct[self.count-1]
                self.revert[self.direct[index]] = index
                self.direct.pop(self.count-1)
            self.count -= 1
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = math.floor(random.random()*self.count)
        return self.direct[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()