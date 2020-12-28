#Design and implement a data structure for Least Frequently Used (LFU) cache.

#Implement the LFUCache class:

#LFUCache(int capacity) Initializes the object with the capacity of the data structure.
#int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
#void put(int key, int value) Sets or inserts the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be evicted.
#Notice that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.



#Example 1:

#Input
#["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
#[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
#Output
#[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

#Explanation
#LFUCache lfu = new LFUCache(2);
#lfu.put(1, 1);
#lfu.put(2, 2);
#lfu.get(1);      // return 1
#lfu.put(3, 3);   // evicts key 2
#lfu.get(2);      // return -1 (not found)
#lfu.get(3);      // return 3
#lfu.put(4, 4);   // evicts key 1.
#lfu.get(1);      // return -1 (not found)
#lfu.get(3);      // return 3
#lfu.get(4);      // return 4


#Constraints:

#0 <= capacity, key, value <= 104
#At most 105 calls will be made to get and put.

from collections import defaultdict, OrderedDict
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.freq2node = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                k,v = self.freq2node[self.min_freq].popitem(last=False)
                self.cache.pop(k)
            node = Node(key, value)
            self.cache[key] = node
            self.freq2node[1][key] = value
            self.min_freq = 1
        else:
            node = self.cache[key]
            node.val = value
            self.update(node)

    def update(self, node):
        k, f = node.key, node.freq
        self.freq2node[f].pop(k)

        node.freq += 1
        self.freq2node[node.freq][k] = node.val

        if not self.freq2node[self.min_freq]:
            self.min_freq += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

node = Node(1,1,1)

