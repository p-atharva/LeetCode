class TrieNode:
    def __init__(self):
        self.children = {}      #hashmap
        self.endWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr_ptr = self.root                                #pointing to the rootnode

        for ch in word:                      #looping through each character of the input word
            if ch not in curr_ptr.children:   #checking if that char is already present or not 
                curr_ptr.children[ch] = TrieNode()   #if not, then create new node with that ch
            curr_ptr = curr_ptr.children[ch]         #else, if already present, update ptr
        
        curr_ptr.endWord = True             #after loop, set the endWord flag to true

    def search(self, word: str) -> bool:
        def dfs(k, node):
            cur_ptr = node

            for i in range(k, len(word)):      #iterating through each char in input word
                ch = word[i]

                # 2 conditions -> if we get "." or not   
                if ch == ".":
                    for child in cur_ptr.children.values():  #take each child and explore
                        if dfs(i+1, child):                  #backtrack after exploration
                            return True
                    return False
                else:
                    if ch not in cur_ptr.children:   #char not present in children of currnode 
                        return False
                    cur_ptr = cur_ptr.children[ch]   #if present move to that node, i++ auto
            return cur_ptr.endWord         #for finished, we return the last node's flag


        return dfs(0, self.root) 


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)