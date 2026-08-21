class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        answer = []
        def dfs(index,path):
            if index == n:
                answer.append(path.copy())
                return
            for i in range(index,len(s)):
                substring = s[index:i+1]
                if substring == substring[::-1]:
                    path.append(substring)
                    dfs(i+1,path)
                    path.pop()
        dfs(0,[])
        return answer

                
        
        