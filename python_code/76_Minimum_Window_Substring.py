#Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

#Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.



#Example 1:

#Input: s = "ADOBECODEBANC", t = "ABC"
#Output: "BANC"
#Example 2:

#Input: s = "a", t = "a"
#Output: "a"


#Constraints:

#1 <= s.length, t.length <= 105
#s and t consist of English letters.

import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        left, right = 0, 0
        window = {}
        needs = {}
        start = 0
        match = 0
        minLen = sys.maxsize + 1

        for c in t:
            if c in needs:
                needs[c] += 1
            else:
                needs[c] = 1

        while right < len(s):
            c = s[right]

            if c in needs:
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1
                if needs[c] == window[c]:
                    match += 1
            right += 1

            while match == len(needs):
                if right - left < minLen:
                    start = left
                    minLen = right - left

                c = s[left]
                if c in needs:
                    window[c] -= 1
                    if window[c] < needs[c]:
                        match -= 1
                left += 1
        return "" if minLen == (sys.maxsize+1) else s[start:start+minLen]


tmp = Solution()
s = "ab"
t = "a"
tmp.minWindow(s, t)
