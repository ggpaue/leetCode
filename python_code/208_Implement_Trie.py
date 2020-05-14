#Implement a trie with insert, search, and startsWith methods.

#Example:

#Trie trie = new Trie();

#trie.insert("apple");
#trie.search("apple");   // returns true
#trie.search("app");     // returns false
#trie.startsWith("app"); // returns true
#trie.insert("app");
#trie.search("app");     // returns true
#Note:

#You may assume that all inputs are consist of lowercase letters a-z.
#All inputs are guaranteed to be non-empty strings.

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t["-"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.trie
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return "-" in t

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)