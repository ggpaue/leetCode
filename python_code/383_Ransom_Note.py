#Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

#Each letter in the magazine string can only be used once in your ransom note.

#Note:
#You may assume that both strings contain only lowercase letters.

#canConstruct("a", "b") -> false
#canConstruct("aa", "ab") -> false
#canConstruct("aa", "aab") -> true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = {}
        magazine_dict = {}

        for ch in ransomNote:
            if ch in ransom_dict:
                ransom_dict[ch] += 1
            else:
                ransom_dict[ch] = 1
        for ch in magazine:
            if ch in magazine_dict:
                magazine_dict[ch] += 1
            else:
                magazine_dict[ch] = 1

        for key in ransom_dict:
            if key in magazine_dict and ransom_dict[key] <= magazine_dict[key]:
                continue
            else:
                return False
        return True
