class PrefixTree:

    def __init__(self):
        self.children = {}
        self.endofword = False
        

    def insert(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = PrefixTree()
            curr = curr.children[ch]
        curr.endofword = True


    def search(self, word: str) -> bool:
        curr = self
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.endofword
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True
        
        