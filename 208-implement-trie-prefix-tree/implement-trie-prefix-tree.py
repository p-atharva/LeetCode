class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        #Initialized the 1st empty Node
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        ptr = self.root

        #Checking character by character whether it is present in the Trie or not
        for ch in word:
            if ch not in ptr.children:
                ptr.children[ch] = TrieNode()
            ptr = ptr.children[ch]
        ptr.end = True                                #marking the end, to understand completion of insertion 

        

    def search(self, word: str) -> bool:
        ptr = self.root

        #checking char by char letter present or not
        for ch in word:
            if ch not in ptr.children:
                return False
            ptr = ptr.children[ch]
        
        return ptr.end
        

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root

        for ch in prefix:
            if ch not in ptr.children:
                return False
            ptr = ptr.children[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)