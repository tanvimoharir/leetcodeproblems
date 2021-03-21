#208. Implement Trie (Prefix Tree)
#Leetcode solution

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children={}
        self.isEnd=False
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node=self
        for letter in word:
            if letter not in node.children:
                node.children[letter]=Trie()
            node=node.children[letter]
        node.isEnd=True
    
    def prefix(self,word:str):
        node=self
        for letter in word:
            if letter not in node.children:
                return None
            node=node.children[letter]
        return node
            
            
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node=self.prefix(word)
        if not node:
            return False
        else:
            return True if node.isEnd else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node=self.prefix(prefix)
        return bool(node)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
