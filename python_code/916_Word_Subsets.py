#We are given two arrays A and B of words.  Each word is a string of lowercase letters.

#Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

#Now say a word a from A is universal if for every b in B, b is a subset of a.

#Return a list of all universal words in A.  You can return the words in any order.



#Example 1:

#Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
#Output: ["facebook","google","leetcode"]
#Example 2:

#Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
#Output: ["apple","google","leetcode"]
#Example 3:

#Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
#Output: ["facebook","google"]
#Example 4:

#Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
#Output: ["google","leetcode"]
#Example 5:

#Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
#Output: ["facebook","leetcode"]


#Note:

#1 <= A.length, B.length <= 10000
#1 <= A[i].length, B[i].length <= 10
#A[i] and B[i] consist only of lowercase letters.
#All words in A[i] are unique: there isn't i != j with A[i] == A[j].

from typing import List
from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        '''

        :param A:
        :param B:
        :return:
                tmp = {}
        res = []
        cmax = 0

        for word in B:
            for char in word:
                cnt = word.count(char)
                if char in tmp:
                    diff = cnt - tmp[char]
                    if diff > 0:
                        tmp[char] = cnt
                        cmax += diff
                else:
                    tmp[char] = cnt
                    cmax += cnt
            if cmax > 10:
                return res

        for word in A:
            if len(word) < cmax:
                continue
            for char in tmp:
                if word.count(char) < tmp[char]:
                    break
            res.append(word)
        return res
        '''

        tmp = Counter()
        for word in B:
            tmp |= Counter(word)

        if sum(tmp.values()) > 10: return []

        return [word for word in A if not tmp-Counter(word)]
