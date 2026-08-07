class WordDictionary:

    def __init__(self):
        self.children = {}
        self.endofword = False
        

    def addWord(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = WordDictionary()
            curr = curr.children[ch]
        curr.endofword = True
        

    def search(self, word: str) -> bool:
        def dfs(index,curr):
            if index == len(word):
                return curr.endofword
            ch = word[index]
            if ch != '.':
                if ch not in curr.children:
                    return False
                return dfs(index+1,curr.children[ch])
            else:
                for child in curr.children.values():
                    if dfs(index+1,child) is True:
                        return True
                return False
        return dfs(0,self)
        
