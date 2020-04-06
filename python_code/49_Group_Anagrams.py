#Given an array of strings, group anagrams together.

#Example:

#Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
#Output:
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]
#Note:

#All inputs will be in lowercase.
#The order of your output does not matter.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            key = sorted(s)
            res[tuple(key)].append(s)
        print(res.values())
        return res.values()

s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s.groupAnagrams(strs)

s="ate"
key=sorted(s)
print(key)
key_tuple = tuple(key)
print(key_tuple)
