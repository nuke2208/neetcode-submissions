class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        word = []
        for i in range(min(n,m)):
            word.append(word1[i])
            word.append(word2[i])
        if m>n:
            for i in range(n,m):
                word.append(word2[i])
        else:
            for i in range(m,n):
                word.append(word1[i])
        return ''.join(word)
        